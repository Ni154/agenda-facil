from fastapi import APIRouter
from datetime import datetime

from config.database import (
    vendas_collection,
    despesas_collection
)

router = APIRouter()

@router.get("/")
def relatorio_geral():
    vendas = list(vendas_collection.find({"status": "finalizada"}))
    despesas = list(despesas_collection.find())

    total_vendas = sum(v.get("valor_total", 0) for v in vendas)
    total_despesas = sum(d.get("valor", 0) for d in despesas)

    return {
        "periodo": {
            "inicio": None,
            "fim": None
        },
        "total_vendas": total_vendas,
        "total_despesas": total_despesas,
        "resultado": total_vendas - total_despesas,
        "quantidade_vendas": len(vendas),
        "quantidade_despesas": len(despesas),
        "gerado_em": datetime.utcnow()
    }
