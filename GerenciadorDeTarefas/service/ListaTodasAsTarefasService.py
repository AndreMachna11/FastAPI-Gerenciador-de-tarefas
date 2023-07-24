from BancoDeDados.poolDeConexoes import postgreSQL_pool_geral
import pandas

class ListaTodasAsTarefasService():
    
    def get_tarefas(self):
        
        conn_geral = postgreSQL_pool_geral.getconn()

        query = f"""
            SELECT 
                *
            FROM
                lista_tarefas
        """
        df = pandas.read_sql(query,conn_geral)

        postgreSQL_pool_geral.putconn(conn_geral)

        return df




