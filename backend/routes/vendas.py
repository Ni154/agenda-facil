from fastapi import APIRouter, HTTPException
from bson import ObjectId
from datetime import datetime

from config.database import (
    vendas_collection,
    agendamentos_collection,
    produtos_collection,
    servicos_collection
)

router = APIRouter()

# Helper
def venda_serializer(venda) -> dict:
    return {
        "id": str(venda["_id"]),
        "agendamento_id": str(venda["agendamento_id"]),
        "cliente_nome": venda.get("cliente_nome"),
        "itens": venda.get("itens", []),
        "valor_total": venda.get("valor_total"),
        "status": venda.get("status"),
        "criado_em": venda.get("criado_em"),
        "finalizado_em": venda.get("finalizado_em")
    }

# LISTAR VENDAS
@router.get("/")
def listar_vendas():
    vendas = vendas_collection.find()
    return [venda_serializer(v) for v in vendas]

# CRIAR PRÉ-VENDA A PARTIR DE AGENDAMENTO
@router.post("/pre-venda/{agendamento_id}")
def criar_pre_venda(agendamento_id: str):
    agendamento = agendamentos_collection.find_one({"_id": ObjectId(agendamento_id)})
    if not agendamento:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")

    venda = {
        "agendamento_id": agendamento["_id"],
        "cliente_nome": agendamento.get("cliente_nome"),
        "itens": [
            {
                "tipo": "servico",
                "servico_id": agendamento["servico_id"],
                "descricao": agendamento.get("servico_nome"),
                "valor": 0
            }
        ],
        "valor_total": 0,
        "status": "pre-venda",  # pre-venda | finalizada | cancelada
        "criado_em": datetime.utcnow(),
        "finalizado_em": None
    }

    result = vendas_collection.insert_one(venda)
    venda["_id"] = result.inserted_id

    # Marca agendamento como faturado (em edição)
    agendamentos_collection.update_one(
        {"_id": agendamento["_id"]},
        {"$set": {"status": "faturado"}}
    )

    return venda_serializer(venda)

# ADICIONAR PRODUTO À VENDA
@router.post("/{venda_id}/produto")
def adicionar_produto(venda_id: str, dados: dict):
    venda = vendas_collection.find_one({"_id": ObjectId(venda_id)})
    if not venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada")

    produto = produtos_collection.find_one({"_id": ObjectId(dados.get("produto_id"))})
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    item = {
        "tipo": "produto",
        "produto_id": produto["_id"],
        "descricao": produto.get("nome"),
        "quantidade": dados.get("quantidade", 1),
        "valor": produto.get("preco")
    }

    vendas_collection.update_one(
        {"_id": venda["_id"]},
        {"$push": {"itens": item}}
    )

    return {"status": "Produto adicionado à venda"}

# ATUALIZAR VALOR DO SERVIÇO NA PRÉ-VENDA
@router.put("/{venda_id}/servico")
def atualizar_valor_servico(venda_id: str, dados: dict):
    venda = vendas_collection.find_one({"_id": ObjectId(venda_id)})
    if not venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada")

    for item in venda["itens"]:
        if item["tipo"] == "servico":
            item["valor"] = dados.get("valor")

    vendas_collection.update_one(
        {"_id": venda["_id"]},
        {"$set": {"itens": venda["itens"]}}
    )

    return {"status": "Serviço atualizado"}

# FINALIZAR VENDA
@router.post("/{venda_id}/finalizar")
def finalizar_venda(venda_id: str):
    venda = vendas_collection.find_one({"_id": ObjectId(venda_id)})
    if not venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada")

    total = 0
    for item in venda["itens"]:
        if item["tipo"] == "produto":
            total += item["valor"] * item.get("quantidade", 1)
        else:
            total += item["valor"]

    vendas_collection.update_one(
        {"_id": venda["_id"]},
        {
            "$set": {
                "valor_total": total,
                "status": "finalizada",
                "finalizado_em": datetime.utcnow()
            }
        }
    )

    venda_atualizada = vendas_collection.find_one({"_id": ObjectId(venda_id)})
    return venda_serializer(venda_atualizada)
