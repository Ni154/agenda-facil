from datetime import datetime

def build_cliente(dados: dict) -> dict:
    """
    Constrói o dicionário padrão de Cliente,
    mantendo compatibilidade total com as rotas existentes.
    """
    return {
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
            "observacoes": dados.get("anamnese", {}).get("observacoes"),
        },
        "criado_em": datetime.utcnow()
    }


def serialize_cliente(cliente: dict) -> dict:
    """
    Serializa Cliente para resposta de API.
    Não altera contrato das rotas.
    """
    return {
        "id": str(cliente.get("_id")),
        "nome": cliente.get("nome"),
        "telefone": cliente.get("telefone"),
        "email": cliente.get("email"),
        "data_nascimento": cliente.get("data_nascimento"),
        "observacoes": cliente.get("observacoes"),
        "anamnese": cliente.get("anamnese", {}),
        "criado_em": cliente.get("criado_em")
    }

