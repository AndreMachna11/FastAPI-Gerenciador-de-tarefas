from fastapi import FastAPI

from GerenciadorDeTarefas.views import CriaOuAtualizaTarefaController
from GerenciadorDeTarefas.views import DadosTarefasController
from GerenciadorDeTarefas.views import ExluirTarefaController
from GerenciadorDeTarefas.views import ListaTodasAsTarefasController

app = FastAPI()
app.include_router(CriaOuAtualizaTarefaController.router)
app.include_router(DadosTarefasController.router)
app.include_router(ListaTodasAsTarefasController.router)
app.include_router(ExluirTarefaController.router)