from datetime import datetime
from uuid import uuid4

from fastapi.openapi.utils import status_code_ranges
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Uuid, MetaData, Table
from sqlalchemy.orm import declarative_base

postgres_db_url = "postgresql://postgres:postgres@localhost/oltp_db"


meta_data = MetaData()

engine = create_engine(postgres_db_url, echo=False)


Base = declarative_base()

class Deployment(Base):
    __tablename__ = 'deployment'
    id = Column(Uuid, primary_key=True, default=str(uuid4()))
    db_name = Column(String(50))
    status = Column(String(50), nullable=False)
    username = Column(String(50))
    creation_time = Column(DateTime)

try:
    conn = engine.connect()
    print('Connected')
    print('connection object is:{}'.format(conn))
except:
    print('Connection failed')

Base.metadata.create_all(engine)
