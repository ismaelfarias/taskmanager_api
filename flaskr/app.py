from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS, cross_origin
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Update
from model import Session, Task
from schemas import *
from logger import logger

info = Info(title="Task Manager API", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)

# Tags
home_tag = Tag(
    name="Documentação",
    description="Seleção de documentação: Swagger, Redoc ou RapiDoc",
)
tasks_tag = Tag(
    name="Tasks", description="Adição, Visualização e remoção de tarefas à base"
)


@app.get("/", tags=[home_tag])
def home():
    return redirect("/openapi")


@app.get("/tasks", responses={"200": TaskListSchema}, tags=[tasks_tag])
def get_tasks():
    """
    Retorna todas as tarefas cadastradas.

    Retorna a listagem de tarefas cadastradas na base de dados, caso a base
    esteja vazia, retorna a task de exemplo a ser exibida no Front End.
    """
    logger.debug(f"Buscando Tarefas ")

    session = Session()

    tasks = session.query(Task).all()

    if not tasks:
        return {"tasks": []}, 200
    else:
        print(tasks)
        return show_tasks(tasks), 200


@app.get(
    "/task", responses={"200": TaskGetSchema, "404": ErrorSchema}, tags=[tasks_tag]
)
def get_task(query: TaskGetSchema):
    """
    Retorna dados da tarefa de acordo com ID informado
    """
    task_id = query.id
    try:
        # Criando conexão com a base
        session = Session()

        task = session.query(Task).filter(Task.id == task_id).first()

        if task:
            return show_tasks(task), 200
        else:
            logger.warning(f"Tarefa #{task_id} não encontrada")
            return {"message": "Not Found"}, 404
    except Exception as e:
        return {"Error": ErrorSchema}, 400


# Cadastra nova tarefa na base de dados
@app.post("/task", responses={"200": TaskSchema}, tags=[tasks_tag])
def add_task(form: TaskSchema):
    """
    Inseri uma nova tarefa no banco de dados
    """
    task = Task(titulo=form.titulo, descricao=form.descricao)
    try:
        # Criando conexão com a base
        session = Session()

        session.add(task)

        session.commit()

        return "sucesso", 200
    except Exception as e:
        return 400


@app.patch("/task", responses={"200": TaskUpdateSchema}, tags=[tasks_tag])
def update_task(form: TaskUpdateSchema):
    """
    Atualiza dados da tarefa conforme o ID informado na requisição
    """
    try:
        session = Session()
        taskupdate = (
            session.query(Task)
            .filter(Task.id == form.id)
            .update(
                {
                    "titulo": form.titulo,
                    "descricao": form.descricao,
                    "status_id": form.status,
                }
            )
        )
        session.commit()

        if taskupdate:
            logger.info(f"Tarefa #{form.id} atualidada.")
            return {"message": "Sucesso"}, 200
        else:
            logger.warning(f"Erro ao atualizar tarefa #{form.id} - Não encontrada.")
            error_msg = f"Tarefa com Id:{form.id} não existe na base de dados"
            return {"message": error_msg}, 404
    except Exception as e:
        return "Falha", e, 400


@app.delete("/task", responses={"200": TaskDelSchema}, tags=[tasks_tag])
def del_task(query: TaskGetSchema):
    """
    Deleta uma tarefa de acordo com o ID informado

    Retorna uma mensagem de confirmação da remoção da exclusão.
    """
    task_id = query.id

    try:
        # Criando conexão com a base
        session = Session()

        # Verifica se existe tarefa com ID informado
        logger.debug(f"Deletando Tarefa #{task_id}")
        count = session.query(Task).filter(Task.id == task_id).delete()

        session.commit()

        if count:
            logger.debug(f"Tarefa #{task_id} Deletada")
            return {"id": task_id, "message": "Deletada"}, 200
        else:
            error_msg = f"Tarefa com Id:{task_id} não existe na base de dados"
            return {"message": error_msg}, 404

    except Exception as e:
        return "Falha", 400
