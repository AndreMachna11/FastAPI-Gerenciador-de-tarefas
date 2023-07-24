from fastapi import APIRouter
from GerenciadorDeTarefas.service.DadosTarefasService import DadosTarefasService

router = APIRouter(prefix="/gerenciador-de-tarefas")

@router.get("/dados-tarefas")
async def retorna_dados_tarefas():
    return 'teste ok'