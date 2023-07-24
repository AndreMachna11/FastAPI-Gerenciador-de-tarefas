from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from Models.tarefa import Tarefa 
from GerenciadorDeTarefas.service.CriaOuAtualizaTarefaService import CriaOuAtualizaTarefaService
from Autenticacao.autenticacao import authenticate

router = APIRouter(prefix="/gerenciador-de-tarefas")

@router.post("/insere-ou-atualiza-tarefa")
async def insere_ou_atualiza_tarefa(tarefa : Tarefa,token : str = Depends(authenticate)):
    
    id_tarefa = tarefa.id_tarefa
    titulo = tarefa.titulo
    descricao = tarefa.descricao
    status = tarefa.status
    
    try:
        SERVICE = CriaOuAtualizaTarefaService()
        SERVICE.upsert_banco_de_dados(id_tarefa, titulo, descricao, status)
        return JSONResponse(content='ok', status_code=200)
    except:
        return JSONResponse(content='internal server error', status_code=500) 
    