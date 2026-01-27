from fastapi import APIRouter
from datetime import datetime
import json
import os

from config.database import (
    clientes_collection,
    produtos_collection,
    servicos_collection,
    agendamentos_collection,
    vendas_collection,
    despesas_collection
)

router = APIRouter()

BACKUP_DIR = "backups"

@router.get("/")
def gerar_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{BACKUP_DIR}/backup_{timestamp}.json"

    data = {
        "clientes": list(clientes_collection.find()),
        "produtos": list(produtos_collection.find()),
        "servicos": list(servicos_collection.find()),
        "agendamentos": list(agendamentos_collection.find()),
        "vendas": list(vendas_collection.find()),
        "despesas": list(despesas_collection.find()),
        "gerado_em": datetime.utcnow().isoformat()
    }

    # Converte ObjectId para string
    def serialize(obj):
        if "_id" in obj:
            obj["_id"] = str(obj["_id"])
        return obj

    for key in data:
        if isinstance(data[key], list):
            data[key] = [serialize(item) for item in data[key]]

    with open(backup_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return {
        "status": "Backup gerado com sucesso",
        "arquivo": backup_file
    }
