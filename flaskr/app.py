from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS, cross_origin
from sqlalchemy.exc import IntegrityError
from model import Session, Task
from schemas import *


info = Info(title="Task Board API", version="0.0.1")
app = OpenAPI(__name__, info=info)

CORS(app)

# Tags
home_tag = Tag(
    name="Documentação",
    description="Seleção de documentação: Swagger, Redoc ou RapiDoc",
)
task_tag = Tag(
    name="Task", description="Adição, visualização e remoção de tarefas à base"
)


@app.get("/", tags=[home_tag])
def home():
    return redirect("/openapi")


"""Retorna todas as tarefas cadastradas"""


@app.get("/tasks", responses={"200": TaskListSchema}, tags=[task_tag])
def get_tasks():

    session = Session()

    tasks = session.query(Task).all()

    if not tasks:
        return {"tasks": [{"id": 1, "titulo": "Exemplo", "status": "New"}]}
    else:
        print(tasks)
        return show_tasks(tasks), 200

@app.get("/task", responses={"200": TaskGetSchema})
def get_task(query: TaskGetSchema):
    task_id = query.id
    print(task_id)
    try:
        # Criando conexão com a base
        session = Session()

        task = session.query(Task).filter(Task.id == task_id)

        return show_tasks(task), 200
    except Exception as e:
        return "Sucesso", 400

# Cadastra nova tarefa na base de dados
@app.post("/task", responses={"200": TaskSchema})
def add_task(form: TaskSchema):
    task = Task(titulo=form.titulo)

    try:
        # Criando conexão com a base
        session = Session()

        session.add(task)

        session.commit()

        return "sucesso", 200
    except Exception as e:
        return 400


@app.delete("/task", responses={"200": TaskGetSchema})
def del_task(query: TaskGetSchema):
    task_id = query.id
    print(task_id)
    try:
        # Criando conexão com a base
        session = Session()

        session.query(Task).filter(Task.id == task_id).delete()

        session.commit()

        return "sucesso", 200
    except Exception as e:
        return "Sucesso", 400
