from pydantic import BaseModel, constr

class TarefaObrigatoria(BaseModel):
    id_tarefa: constr(max_length=100)
    titulo: constr(max_length=255)
    descricao: constr(max_length=1000)
    status: constr(max_length=100)

class TarefaOpcional(BaseModel):
    id_tarefa: constr(max_length=100) = None
    titulo: constr(max_length=255) = None
    descricao: constr(max_length=1000) = None
    status: constr(max_length=100) = None