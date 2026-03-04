import datetime
from uuid import UUID

from pydantic import BaseModel

class Deployment(BaseModel):
    id: UUID
    db_name: str
    status: Status
    username: str
    creation_time: datetime.datetime


class Status(BaseModel):
    created: int = 0
    deleted: int = 1

