from datetime import datetime

def build_servico(dados: dict) -> dict:
    """
    Constrói o dicionário padrão de Serviço.
    Mantém compatibilidade total com as rotas existentes.
    """
    return {
        "nome": dados.get("nome"),
        "descricao": dados.get("descricao"),
        "preco": dados.get("preco"),
        "duracao_minutos": dados.get("duracao_minutos"),
        "ativo": dados.get("ativo", True),
        "criado_em": datetime.utcnow()
    }


def serialize_servico(servico: dict) -> dict:
    """
    Serializa Serviço para resposta da API.
    """
    return {
        "id": str(servico.get("_id")),
        "nome": servico.get("nome"),
        "descricao": servico.get("descricao"),
        "preco": servico.get("preco"),
        "duracao_minutos": servico.get("duracao_minutos"),
        "ativo": servico.get("ativo"),
        "criado_em": servico.get("criado_em")
    }
