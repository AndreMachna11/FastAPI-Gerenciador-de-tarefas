from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from Models.tarefa import TarefaOpcional 
from Autenticacao.autenticacao import authenticate
from GerenciadorDeTarefas.service.DadosTarefasService import DadosTarefasService

router = APIRouter(prefix="/gerenciador-de-tarefas")

@router.post("/dados-tarefas/")
async def retorna_dados_tarefas(tarefa: TarefaOpcional, token : str = Depends(authenticate)):
    id_tarefa = tarefa.id_tarefa
    titulo = tarefa.titulo
    descricao = tarefa.descricao
    status = tarefa.status
    
    try:
        SERVICE = DadosTarefasService()
        retorno = SERVICE.get_dados_tarefa(id_tarefa, titulo, descricao, status)

        if retorno.empty == True:
            return JSONResponse(content='tarefa não encontrada', status_code=400)
        else:
            retorno = retorno.to_dict(orient='records')
            return JSONResponse(content=retorno, status_code=200)
    except:
        return JSONResponse(content='internal server error', status_code=500) 