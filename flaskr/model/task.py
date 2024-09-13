from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from typing import Union
from datetime import datetime

from model import Base

class Task(Base):
    __tablename__ = 'task'

    id = Column("id", Integer, primary_key=True)
    titulo = Column(String(50), nullable=False)
    descricao = Column(String(256), nullable=True)
    status_id = Column(Integer, ForeignKey("status.id"), nullable=False)
    dt_criacao = Column(DateTime, default=datetime.now())
    dt_atualizacao = Column(DateTime, nullable=True)
    dt_conclusao = Column(DateTime, nullable=True)

    def __init__(self, titulo:str,
                 dt_criacao:Union[DateTime, None] = None):
        self.titulo = titulo
        self.dt_criacao = dt_criacao
        self.status_id = 1

        if dt_criacao:
            self.dt_criacao = dt_criacao
