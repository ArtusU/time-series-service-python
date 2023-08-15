import uuid

from fastapi import HTTPException


def validate_id(id: str):
    try:
        _uuid = uuid.UUID(id)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    return _uuid
