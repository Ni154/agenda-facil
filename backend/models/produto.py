from datetime import datetime

def build_produto(dados: dict) -> dict:
    """
    Constrói o dicionário padrão de Produto.
    Não altera nenhuma rota existente.
    """
    return {
        "nome": dados.get("nome"),
        "descricao": dados.get("descricao"),
        "preco": dados.get("preco"),
        "estoque": dados.get("estoque", 0),
        "ativo": dados.get("ativo", True),
        "criado_em": datetime.utcnow()
    }


def serialize_produto(produto: dict) -> dict:
    """
    Serializa Produto para resposta da API.
    """
    return {
        "id": str(produto.get("_id")),
        "nome": produto.get("nome"),
        "descricao": produto.get("descricao"),
        "preco": produto.get("preco"),
        "estoque": produto.get("estoque"),
        "ativo": produto.get("ativo"),
        "criado_em": produto.get("criado_em")
    }
