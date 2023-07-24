# FastAPI-Gerenciador-de-Tarefas

* API desenvolvida usando o framework FastAPI para prover serviços a um gerenciador de tarefas
* Todo o processo de deploy foi feito e sua documentação interativa pode ser acessada em https://
* Serviços AWS utilizados

  -RDS: Para banco de dados postgreSQL

  -Route 53: - Para configuração de dominio e DNS

  -EC2: Para hostear a API

# Instruçoes para Execução

* O Python 3.11 ou superior e o git devem estar instalados em sua maquina. Depois segue-se a sequencia de comandos

```sh
git clone https://github.com/AndreMachna11/FastAPI-Gerenciador-de-tarefas.git
```

```sh
cd FastAPI-Gerenciador-de-tarefas
```

```sh
pip install pipenv
```

```sh
pipenv shell
```

```sh
pipenv install pipfile
```

```sh
uvicorn main:app --reload
```

# Instruçoes para Uso dos endpoints

Todos os endpoints exigem um token no header da requisição, nesta api ele é unico e estatico 
```sh
d9520359df50574372fb8022fb56b90671cbf5c388132953a69b28d5ec37bfb6
```

No endpoint de /gerenciador-de-tarefas/dados-tarefas/ a busca é feita pelo json que é inputado, seguindo uma ordem de prioridade:

-id_tarefa

-titulo

-descricao

-status


Onde se estiver presente no json um de maior prioridade, este será usado

   {
      "id_tarefa": "string",
      "titulo": "string",
      "descricao": "string",
      "status": "string"
    }

    ou 

    {
      "titulo": "string",
      "descricao": "string",
      "status": "string"
    }

    e assim por diante
