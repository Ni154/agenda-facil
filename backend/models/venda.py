from datetime import datetime

def build_pre_venda(agendamento: dict) -> dict:
    """
    Cria uma pré-venda a partir de um agendamento,
    exatamente como o fluxo original do sistema.
    """
    return {
        "agendamento_id": agendamento["_id"],
        "cliente_nome": agendamento.get("cliente_nome"),
        "itens": [
            {
                "tipo": "servico",
                "servico_id": agendamento.get("servico_id"),
                "descricao": agendamento.get("servico_nome"),
                "valor": 0
            }
        ],
        "valor_total": 0,
        "status": "pre-venda",  # pre-venda | finalizada | cancelada
        "criado_em": datetime.utcnow(),
        "finalizado_em": None
    }


def calcular_total(itens: list) -> float:
    """
    Calcula o valor total da venda a partir dos itens.
    """
    total = 0
    for item in itens:
        if item.get("tipo") == "produto":
            total += item.get("valor", 0) * item.get("quantidade", 1)
        else:
            total += item.get("valor", 0)
    return total


def serialize_venda(venda: dict) -> dict:
    """
    Serializa Venda para resposta da API.
    """
    return {
        "id": str(venda.get("_id")),
        "agendamento_id": str(venda.get("agendamento_id")),
        "cliente_nome": venda.get("cliente_nome"),
        "itens": venda.get("itens", []),
        "valor_total": venda.get("valor_total"),
        "status": venda.get("status"),
        "criado_em": venda.get("criado_em"),
        "finalizado_em": venda.get("finalizado_em")
    }
