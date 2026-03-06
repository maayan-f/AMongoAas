from datetime import datetime
from enum import Enum

from fastapi import APIRouter, FastAPI, HTTPException
from sqlalchemy.orm import Session
from deployment.deployment_engine import engine, Deployment

router = APIRouter(
prefix="/deployments"
)

@router.post("")
def create_deployment(db_name, username):
     if db_name.startswith(username):
        with Session(engine) as session:
            spongebob = Deployment(
                db_name=db_name,
                status=Status.create,
                username=username,
                creation_time=datetime.now()
            )
            session.add_all([spongebob])
            print(spongebob)
            session.commit()
            return spongebob.id
        return None
     else:
        raise HTTPException(status_code=400, detail="bad request")
        return None


class Status(str, Enum):
    create = "CREATE"
    deleted = "DELETED"