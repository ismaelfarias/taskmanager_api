from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import os


# Importando elementos definidos no modelo de dados
from model.base import Base
from model.task import Task
from model.status import Status

db_path = "database/"

if not os.path.exists(db_path):
    os.makedirs(db_path)

# String de conexão com o banco de dados
db_url = 'sqlite:///%s/db.sqlite3' % db_path

engine = create_engine(db_url, echo=False)

Session = sessionmaker(bind=engine)


# Cria o banco caso não exista
if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)