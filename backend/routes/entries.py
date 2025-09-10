from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from backend.config.database import get_db
from backend.routes.utils import paginate
from backend.core.security import get_current_user
from backend.models.entry import Entry
from backend.models.change_log import ChangeLog
from backend.schemas.entry import EntryIn, EntryOut
import json
from datetime import datetime

router = APIRouter()

@router.get("")
def list_items(page: int = 1, size: int = 10, q: Optional[str] = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
    query = db.query(Entry).filter(Entry.deleted_at.is_(None))
    if q:
        # naive search by name/description fields if present
        if hasattr(Entry, "name"):
            query = query.filter(Entry.name.ilike(f"%{q}%"))
        elif hasattr(Entry, "description"):
            query = query.filter(Entry.description.ilike(f"%{q}%"))
    items, total = paginate(query, page, size)
    return {"items": [i.__dict__ for i in items], "total": total, "page": page, "size": size}

@router.post("", response_model=EntryOut)
def create_item(payload: EntryIn, db: Session = Depends(get_db), user=Depends(get_current_user)):
    obj = Entry(**payload.dict())
    db.add(obj); db.commit(); db.refresh(obj)
    db.add(ChangeLog(entity="entry", entity_id=obj.id, action="create", before=None, after=json.dumps(payload.dict()), user_id=user.id))
    db.commit()
    return EntryOut(**{**payload.dict(), "id": obj.id})

@router.put("/{item_id}", response_model=EntryOut)
def update_item(item_id: int, payload: EntryIn, db: Session = Depends(get_db), user=Depends(get_current_user)):
    obj = db.query(Entry).filter(Entry.id == item_id, Entry.deleted_at.is_(None)).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Não encontrado")
    before = obj.__dict__.copy()
    for k, v in payload.dict().items():
        setattr(obj, k, v)
    db.commit(); db.refresh(obj)
    db.add(ChangeLog(entity="entry", entity_id=obj.id, action="update", before=json.dumps(before, default=str), after=json.dumps(payload.dict()), user_id=user.id))
    db.commit()
    return EntryOut(**{**payload.dict(), "id": obj.id})

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    obj = db.query(Entry).filter(Entry.id == item_id, Entry.deleted_at.is_(None)).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Não encontrado")
    from sqlalchemy import func
    obj.deleted_at = func.now()
    db.commit()
    db.add(ChangeLog(entity="entry", entity_id=obj.id, action="delete", before=None, after=None, user_id=user.id))
    db.commit()
    return {"ok": True}
