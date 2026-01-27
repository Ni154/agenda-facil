from fastapi import APIRouter, HTTPException
from bson import ObjectId
from datetime import datetime

from config.database import despesas_collection

router = APIRouter()

# Helper
def despesa_serializer(despesa) -> dict:
    return {
        "id": str(despesa["_id"]),
        "descricao": despesa.get("descricao"),
        "categoria": despesa.get("categoria"),
        "valor": despesa.get("valor"),
        "data": despesa.get("data"),
        "observacoes": despesa.get("observacoes"),
        "criado_em": despesa.get("criado_em")
    }

# LISTAR DESPESAS
@router.get("/")
def listar_despesas():
    despesas = despesas_collection.find()
    return [despesa_serializer(d) for d in despesas]

# OBTER DESPESA POR ID
@router.get("/{despesa_id}")
def obter_despesa(despesa_id: str):
    despesa = despesas_collection.find_one({"_id": ObjectId(despesa_id)})
    if not despesa:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    return despesa_serializer(despesa)

# CRIAR DESPESA
@router.post("/")
def criar_despesa(dados: dict):
    despesa = {
        "descricao": dados.get("descricao"),
        "categoria": dados.get("categoria"),
        "valor": dados.get("valor"),
        "data": dados.get("data"),
        "observacoes": dados.get("observacoes"),
        "criado_em": datetime.utcnow()
    }

    result = despesas_collection.insert_one(despesa)
    despesa["_id"] = result.inserted_id
    return despesa_serializer(despesa)

# ATUALIZAR DESPESA
@router.put("/{despesa_id}")
def atualizar_despesa(despesa_id: str, dados: dict):
    update = {
        "descricao": dados.get("descricao"),
        "categoria": dados.get("categoria"),
        "valor": dados.get("valor"),
        "data": dados.get("data"),
        "observacoes": dados.get("observacoes")
    }

    result = despesas_collection.update_one(
        {"_id": ObjectId(despesa_id)},
        {"$set": update}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")

    despesa = despesas_collection.find_one({"_id": ObjectId(despesa_id)})
    return despesa_serializer(despesa)

# EXCLUIR DESPESA
@router.delete("/{despesa_id}")
def excluir_despesa(despesa_id: str):
    result = despesas_collection.delete_one({"_id": ObjectId(despesa_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    return {"status": "Despesa excluída com sucesso"}
