from fastapi import APIRouter, HTTPException
from bson import ObjectId
from datetime import datetime

from config.database import (
    agendamentos_collection,
    clientes_collection,
    servicos_collection
)

router = APIRouter()

# Helper para serializar ObjectId
def agendamento_serializer(agendamento) -> dict:
    return {
        "id": str(agendamento["_id"]),
        "cliente_id": str(agendamento["cliente_id"]),
        "cliente_nome": agendamento.get("cliente_nome"),
        "servico_id": str(agendamento["servico_id"]),
        "servico_nome": agendamento.get("servico_nome"),
        "data_hora": agendamento.get("data_hora"),
        "status": agendamento.get("status"),
        "observacoes": agendamento.get("observacoes"),
        "criado_em": agendamento.get("criado_em")
    }

# LISTAR AGENDAMENTOS
@router.get("/")
def listar_agendamentos():
    agendamentos = agendamentos_collection.find()
    return [agendamento_serializer(a) for a in agendamentos]

# OBTER AGENDAMENTO POR ID
@router.get("/{agendamento_id}")
def obter_agendamento(agendamento_id: str):
    agendamento = agendamentos_collection.find_one({"_id": ObjectId(agendamento_id)})
    if not agendamento:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return agendamento_serializer(agendamento)

# CRIAR AGENDAMENTO
@router.post("/")
def criar_agendamento(dados: dict):
    cliente = clientes_collection.find_one({"_id": ObjectId(dados.get("cliente_id"))})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    servico = servicos_collection.find_one({"_id": ObjectId(dados.get("servico_id"))})
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")

    agendamento = {
        "cliente_id": cliente["_id"],
        "cliente_nome": cliente.get("nome"),
        "servico_id": servico["_id"],
        "servico_nome": servico.get("nome"),
        "data_hora": dados.get("data_hora"),
        "status": "agendado",  # agendado | concluido | cancelado | faturado
        "observacoes": dados.get("observacoes"),
        "criado_em": datetime.utcnow()
    }

    result = agendamentos_collection.insert_one(agendamento)
    agendamento["_id"] = result.inserted_id
    return agendamento_serializer(agendamento)

# ATUALIZAR AGENDAMENTO
@router.put("/{agendamento_id}")
def atualizar_agendamento(agendamento_id: str, dados: dict):
    update = {
        "data_hora": dados.get("data_hora"),
        "status": dados.get("status"),
        "observacoes": dados.get("observacoes")
    }

    result = agendamentos_collection.update_one(
        {"_id": ObjectId(agendamento_id)},
        {"$set": update}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")

    agendamento = agendamentos_collection.find_one({"_id": ObjectId(agendamento_id)})
    return agendamento_serializer(agendamento)

# EXCLUIR AGENDAMENTO
@router.delete("/{agendamento_id}")
def excluir_agendamento(agendamento_id: str):
    result = agendamentos_collection.delete_one({"_id": ObjectId(agendamento_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return {"status": "Agendamento excluído com sucesso"}
