from datetime import datetime

def build_agendamento(cliente: dict, servico: dict, dados: dict) -> dict:
    """
    Constrói o dicionário padrão de Agendamento.
    Mantém o modelo fiel ao fluxo original (agendamento → venda).
    """
    return {
        "cliente_id": cliente["_id"],
        "cliente_nome": cliente.get("nome"),
        "servico_id": servico["_id"],
        "servico_nome": servico.get("nome"),
        "data_hora": dados.get("data_hora"),
        "status": "agendado",  # agendado | concluido | faturado | cancelado
        "observacoes": dados.get("observacoes"),
        "criado_em": datetime.utcnow()
    }


def serialize_agendamento(agendamento: dict) -> dict:
    """
    Serializa Agendamento para resposta da API.
    """
    return {
        "id": str(agendamento.get("_id")),
        "cliente_id": str(agendamento.get("cliente_id")),
        "cliente_nome": agendamento.get("cliente_nome"),
        "servico_id": str(agendamento.get("servico_id")),
        "servico_nome": agendamento.get("servico_nome"),
        "data_hora": agendamento.get("data_hora"),
        "status": agendamento.get("status"),
        "observacoes": agendamento.get("observacoes"),
        "criado_em": agendamento.get("criado_em")
    }
