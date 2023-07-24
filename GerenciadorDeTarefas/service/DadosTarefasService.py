from BancoDeDados.poolDeConexoes import postgreSQL_pool_geral
import pandas


class DadosTarefasService():

    def get_dados_tarefa(self, id_tarefa, titulo, descricao, status):
        
        conn_geral = postgreSQL_pool_geral.getconn()

        if id_tarefa != None:

            query = f"""
                SELECT 
                    *
                FROM
                    lista_tarefas
                WHERE
                    id_tarefa = '{id_tarefa}'
            """
            df = pandas.read_sql(query,conn_geral)

        elif titulo != None:
            query = f"""
                SELECT 
                    *
                FROM
                    lista_tarefas
                WHERE
                    titulo ~ '^({titulo}).*'
            """
            df = pandas.read_sql(query,conn_geral) 

        elif descricao != None:

            query = f"""
                SELECT 
                    *
                FROM
                    lista_tarefas
                WHERE
                    descricao ~ '^({descricao}).*'
            """
            df = pandas.read_sql(query,conn_geral) 

        elif status != None:
            query = f"""
                SELECT 
                    *
                FROM
                    lista_tarefas
                WHERE
                    status ~ '^({status}).*'
            """
            df = pandas.read_sql(query,conn_geral) 

        else:
            df = pandas.DataFrame()

        postgreSQL_pool_geral.putconn(conn_geral)
        
        return df
      
       

        
    