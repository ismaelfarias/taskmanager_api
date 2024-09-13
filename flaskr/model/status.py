from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from typing import Union

from model import Base

class Status(Base):
    __tablename__ = 'status'

    id = Column("id", Integer, primary_key=True)
    descricao = Column(String(50), nullable=False)

    def __init__(self, id:int, descricao:str):
        self.id = id
        self.descricao = descricao
