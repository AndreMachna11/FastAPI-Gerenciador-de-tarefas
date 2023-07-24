from pydantic import BaseModel, constr

class Tarefa(BaseModel):
    id_tarefa: constr(max_length=100)
    titulo: constr(max_length=255)
    descricao: constr(max_length=1000)
    status: constr(max_length=100)

