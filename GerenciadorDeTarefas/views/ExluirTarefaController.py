from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from Autenticacao.autenticacao import authenticate
from GerenciadorDeTarefas.service.ExluirTarefaService import ExluirTarefaService

router = APIRouter(prefix="/gerenciador-de-tarefas")

@router.delete("/excluir-tarefas{id_tarefa}")
async def excluir_tarefas(id_tarefa: str,token: str = Depends(authenticate)):

    try:
        SERVICE = ExluirTarefaService() 
        SERVICE.delete_banco_de_dados(id_tarefa)
        return JSONResponse(content='ok', status_code=200) 
    except:
        return JSONResponse(content='internal server error', status_code=500) 
