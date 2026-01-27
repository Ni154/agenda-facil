from fastapi import APIRouter, HTTPException
from bson import ObjectId
from datetime import datetime

from config.database import clientes_collection

router = APIRouter()

# Helper para serializar ObjectId
def cliente_serializer(cliente) -> dict:
    return {
        "id": str(cliente["_id"]),
        "nome": cliente.get("nome"),
        "telefone": cliente.get("telefone"),
        "email": cliente.get("email"),
        "data_nascimento": cliente.get("data_nascimento"),
        "observacoes": cliente.get("observacoes"),
        "anamnese": cliente.get("anamnese", {}),
        "criado_em": cliente.get("criado_em")
    }

# LISTAR CLIENTES
@router.get("/")
def listar_clientes():
    clientes = clientes_collection.find()
    return [cliente_serializer(cliente) for cliente in clientes]

# OBTER CLIENTE POR ID
@router.get("/{cliente_id}")
def obter_cliente(cliente_id: str):
    cliente = clientes_collection.find_one({"_id": ObjectId(cliente_id)})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente_serializer(cliente)

# CRIAR CLIENTE (COM ANAMNESE)
@router.post("/")
def criar_cliente(dados: dict):
    cliente = {
        "nome": dados.get("nome"),
        "telefone": dados.get("telefone"),
        "email": dados.get("email"),
        "data_nascimento": dados.get("data_nascimento"),
        "observacoes": dados.get("observacoes"),
        "anamnese": {
            "alergias": dados.get("anamnese", {}).get("alergias"),
            "doencas": dados.get("anamnese", {}).get("doencas"),
            "medicamentos": dados.get("anamnese", {}).get("medicamentos"),
            "procedimentos_anteriores": dados.get("anamnese", {}).get("procedimentos_anteriores"),
            "observacoes": dados.get("anamnese", {}).get("observacoes")
        },
        "criado_em": datetime.utcnow()
    }

    result = clientes_collection.insert_one(cliente)
    cliente["_id"] = result.inserted_id
    return cliente_serializer(cliente)

# ATUALIZAR CLIENTE (INCLUINDO ANAMNESE)
@router.put("/{cliente_id}")
def atualizar_cliente(cliente_id: str, dados: dict):
    update = {
        "nome": dados.get("nome"),
        "telefone": dados.get("telefone"),
        "email": dados.get("email"),
        "data_nascimento": dados.get("data_nascimento"),
        "observacoes": dados.get("observacoes"),
        "anamnese": dados.get("anamnese")
    }

    result = clientes_collection.update_one(
        {"_id": ObjectId(cliente_id)},
        {"$set": update}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    cliente = clientes_collection.find_one({"_id": ObjectId(cliente_id)})
    return cliente_serializer(cliente)

# EXCLUIR CLIENTE
@router.delete("/{cliente_id}")
def excluir_cliente(cliente_id: str):
    result = clientes_collection.delete_one({"_id": ObjectId(cliente_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"status": "Cliente excluído com sucesso"}
