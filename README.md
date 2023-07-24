# FastAPI-Gerenciador-de-Tarefas

* API desenvolvida usando o framework FastAPI para prover serviços a um gerenciador de tarefas
* Todo o processo de deploy foi feito e sua documentação interativa pode ser acessada em https://gerenciador-tarefas.dev-andre-machna.com.br/docs
* Serviços AWS utilizados

  -RDS: Para banco de dados postgreSQL

  -Route 53: - Para configuração de dominio e DNS

  -EC2: Para hostear a API

# Instruçoes para Execução Local

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


Onde se estiver presente no json um de maior prioridade, este será usado, por exemplo:


    {
      "id_tarefa": "string",
      "titulo": "string",
      "descricao": "string",
      "status": "string"
    }

id_tarefa será usado na busca 

    {
      "titulo": "string",
      "descricao": "string",
      "status": "string"
    }

titulo será usado na busca

    {
      "descricao": "string",
      "status": "string"
    }

descrição será usado na busca, e assim por diante

Todos os outro enpoints o proprio Swagger em https://gerenciador-tarefas.dev-andre-machna.com.br/docs ja se faz suficiente
