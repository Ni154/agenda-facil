from typing import Tuple
from sqlalchemy.orm import Query

def paginate(query: Query, page: int = 1, size: int = 10) -> Tuple[list, int]:
    total = query.count()
    items = query.offset((page-1)*size).limit(size).all()
    return items, total
