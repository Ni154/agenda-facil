from fastapi import APIRouter, HTTPException
from bson import ObjectId
from datetime import datetime

from config.database import produtos_collection

router = APIRouter()

# Helper para serializar ObjectId
def produto_serializer(produto) -> dict:
    return {
        "id": str(produto["_id"]),
        "nome": produto.get("nome"),
        "descricao": produto.get("descricao"),
        "preco": produto.get("preco"),
        "estoque": produto.get("estoque"),
        "ativo": produto.get("ativo", True),
        "criado_em": produto.get("criado_em")
    }

# LISTAR PRODUTOS
@router.get("/")
def listar_produtos():
    produtos = produtos_collection.find()
    return [produto_serializer(produto) for produto in produtos]

# OBTER PRODUTO POR ID
@router.get("/{produto_id}")
def obter_produto(produto_id: str):
    produto = produtos_collection.find_one({"_id": ObjectId(produto_id)})
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto_serializer(produto)

# CRIAR PRODUTO
@router.post("/")
def criar_produto(dados: dict):
    produto = {
        "nome": dados.get("nome"),
        "descricao": dados.get("descricao"),
        "preco": dados.get("preco"),
        "estoque": dados.get("estoque", 0),
        "ativo": True,
        "criado_em": datetime.utcnow()
    }

    result = produtos_collection.insert_one(produto)
    produto["_id"] = result.inserted_id
    return produto_serializer(produto)

# ATUALIZAR PRODUTO
@router.put("/{produto_id}")
def atualizar_produto(produto_id: str, dados: dict):
    update = {
        "nome": dados.get("nome"),
        "descricao": dados.get("descricao"),
        "preco": dados.get("preco"),
        "estoque": dados.get("estoque"),
        "ativo": dados.get("ativo", True)
    }

    result = produtos_collection.update_one(
        {"_id": ObjectId(produto_id)},
        {"$set": update}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    produto = produtos_collection.find_one({"_id": ObjectId(produto_id)})
    return produto_serializer(produto)

# EXCLUIR PRODUTO
@router.delete("/{produto_id}")
def excluir_produto(produto_id: str):
    result = produtos_collection.delete_one({"_id": ObjectId(produto_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"status": "Produto excluído com sucesso"}
