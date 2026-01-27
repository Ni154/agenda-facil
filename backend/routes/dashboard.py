from fastapi import APIRouter
from config.database import (
    clientes_collection,
    vendas_collection,
    despesas_collection
)

router = APIRouter()

@router.get("/")
def obter_dashboard():
    total_clientes = clientes_collection.count_documents({})
    total_vendas = vendas_collection.count_documents({"status": "finalizada"})
    total_despesas = despesas_collection.count_documents({})

    valor_vendas = 0
    for v in vendas_collection.find({"status": "finalizada"}):
        valor_vendas += v.get("valor_total", 0)

    valor_despesas = 0
    for d in despesas_collection.find():
        valor_despesas += d.get("valor", 0)

    return {
        "total_clientes": total_clientes,
        "total_vendas": total_vendas,
        "total_despesas": total_despesas,
        "valor_vendas": valor_vendas,
        "valor_despesas": valor_despesas,
        "resultado": valor_vendas - valor_despesas
    }
