from fastapi import APIRouter, HTTPException
from bson import ObjectId
from datetime import datetime

from config.database import servicos_collection

router = APIRouter()

# Helper para serializar ObjectId
def servico_serializer(servico) -> dict:
    return {
        "id": str(servico["_id"]),
        "nome": servico.get("nome"),
        "descricao": servico.get("descricao"),
        "preco": servico.get("preco"),
        "duracao_minutos": servico.get("duracao_minutos"),
        "ativo": servico.get("ativo", True),
        "criado_em": servico.get("criado_em")
    }

# LISTAR SERVIÇOS
@router.get("/")
def listar_servicos():
    servicos = servicos_collection.find()
    return [servico_serializer(servico) for servico in servicos]

# OBTER SERVIÇO POR ID
@router.get("/{servico_id}")
def obter_servico(servico_id: str):
    servico = servicos_collection.find_one({"_id": ObjectId(servico_id)})
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    return servico_serializer(servico)

# CRIAR SERVIÇO
@router.post("/")
def criar_servico(dados: dict):
    servico = {
        "nome": dados.get("nome"),
        "descricao": dados.get("descricao"),
        "preco": dados.get("preco"),
        "duracao_minutos": dados.get("duracao_minutos"),
        "ativo": True,
        "criado_em": datetime.utcnow()
    }

    result = servicos_collection.insert_one(servico)
    servico["_id"] = result.inserted_id
    return servico_serializer(servico)

# ATUALIZAR SERVIÇO
@router.put("/{servico_id}")
def atualizar_servico(servico_id: str, dados: dict):
    update = {
        "nome": dados.get("nome"),
        "descricao": dados.get("descricao"),
        "preco": dados.get("preco"),
        "duracao_minutos": dados.get("duracao_minutos"),
        "ativo": dados.get("ativo", True)
    }

    result = servicos_collection.update_one(
        {"_id": ObjectId(servico_id)},
        {"$set": update}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")

    servico = servicos_collection.find_one({"_id": ObjectId(servico_id)})
    return servico_serializer(servico)

# EXCLUIR SERVIÇO
@router.delete("/{servico_id}")
def excluir_servico(servico_id: str):
    result = servicos_collection.delete_one({"_id": ObjectId(servico_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    return {"status": "Serviço excluído com sucesso"}
