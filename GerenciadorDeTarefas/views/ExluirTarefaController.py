from fastapi import APIRouter
from GerenciadorDeTarefas.service.ExluirTarefaService import ExluirTarefaService

router = APIRouter(prefix="/gerenciador-de-tarefas")

@router.get("/excluir-tarefas")
async def excluir_tarefas():
    return 'teste ok'