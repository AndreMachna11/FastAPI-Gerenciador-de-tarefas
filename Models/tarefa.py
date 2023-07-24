from pydantic import BaseModel, constr

#Objeto para uso no endpoint de upsert
class TarefaObrigatoria(BaseModel):
    id_tarefa: constr(max_length=100)
    titulo: constr(max_length=255)
    descricao: constr(max_length=1000)
    status: constr(max_length=100)

#Objeto para uso no endpoint de busca por dados de um tarefa especifica e por qrr dado
class TarefaOpcional(BaseModel):
    id_tarefa: constr(max_length=100) = None
    titulo: constr(max_length=255) = None
    descricao: constr(max_length=1000) = None
    status: constr(max_length=100) = None