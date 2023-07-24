from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from Autenticacao.autenticacao import authenticate
from GerenciadorDeTarefas.service.ListaTodasAsTarefasService import ListaTodasAsTarefasService

router = APIRouter(prefix="/gerenciador-de-tarefas")

@router.get("/listar-tarefas")
async def listar_tarefas(token : str = Depends(authenticate)):
    
    try:
        SERVICE = ListaTodasAsTarefasService()
        retorno = SERVICE.get_tarefas()
        retorno = retorno.to_dict(orient='records')
        return JSONResponse(content=retorno, status_code=200)
    
    except:
        return JSONResponse(content='internal server error', status_code=500) 