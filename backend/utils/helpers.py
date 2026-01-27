from bson import ObjectId

def to_object_id(id_str: str):
    """
    Converte string para ObjectId com segurança.
    """
    try:
        return ObjectId(id_str)
    except Exception:
        return None


def serialize_object_id(data: dict) -> dict:
    """
    Converte ObjectId em string dentro de um dicionário.
    """
    if "_id" in data:
        data["_id"] = str(data["_id"])
    return data


def serialize_list(data_list: list) -> list:
    """
    Serializa uma lista de documentos MongoDB.
    """
    return [serialize_object_id(item) for item in data_list]
