from datetime import datetime

def build_despesa(dados: dict) -> dict:
    """
    Constrói o dicionário padrão de Despesa.
    """
    return {
        "descricao": dados.get("descricao"),
        "categoria": dados.get("categoria"),
        "valor": dados.get("valor"),
        "data": dados.get("data"),
        "observacoes": dados.get("observacoes"),
        "criado_em": datetime.utcnow()
    }


def serialize_despesa(despesa: dict) -> dict:
    """
    Serializa Despesa para resposta da API.
    """
    return {
        "id": str(despesa.get("_id")),
        "descricao": despesa.get("descricao"),
        "categoria": despesa.get("categoria"),
        "valor": despesa.get("valor"),
        "data": despesa.get("data"),
        "observacoes": despesa.get("observacoes"),
        "criado_em": despesa.get("criado_em")
    }
