from pydantic import BaseModel
from typing import Optional, List
from model.task import Task

#from schemas import StatusSchema

class TaskSchema(BaseModel):
    """ Define como uma nova tarefa deve ser representada"""
    titulo: str = "Estudar Python"
    descricao: str = "Descrição da Tarefa"

class TaskListSchema(BaseModel):
    """ Define como a listagem de tarefas será retornada.
    """
    tarefas:List[TaskSchema]

class TaskGetSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca realizada com base no id da tarefa"""
    id: int = 1

def show_tasks(tasks: List[Task]):
    """ Retorna uma representação da tarefa conforme o schema definido em
        GetTaskSchema.
    """
    result = []
    for task in tasks:
        result.append({
            "id": task.id,
            "titulo": task.titulo,
            "descricao": task.descricao,
            "status": task.status_id,
            "dt_criacao": task.dt_criacao,
            "dt_atualizacao": task.dt_atualizacao,
            "dt_conclusao": task.dt_conclusao
        })

    return {"tasks": result}

class TaskDelSchema(BaseModel):
    """ 
    Define comom deve ser a estrutura do dado retornado apóss uma requisição de remoção.
    """
    id: int = 1
    message: str = "Deletado"

class TaskUpdateSchema(BaseModel):
    id: int = 1
    titulo: str = "Titulo da Tarefa"
    descricao: str = "Descricao da Tarefa"
    status: int = 1
