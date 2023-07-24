from fastapi import APIRouter
from GerenciadorDeTarefas.service.ListaTodasAsTarefasService import ListaTodasAsTarefasService

router = APIRouter(prefix="/gerenciador-de-tarefas")

@router.get("/listar-tarefas")
async def listar_tarefas():
    return 'teste ok'