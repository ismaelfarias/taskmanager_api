from pydantic import BaseModel

class StatusSchema(BaseModel):
    """ Define a entidade que armazena o código de status da tarefas
    """
    status_id: int = 1
    descricao: str = "Defini o status da tarefa"
