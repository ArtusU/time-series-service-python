import uuid
from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str


class Device(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str


class DataPoint(BaseModel):
    timestamp: datetime
    value: float
    device: Device
    user: User
