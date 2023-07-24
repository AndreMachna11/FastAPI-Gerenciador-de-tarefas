from BancoDeDados.poolDeConexoes import postgreSQL_pool_geral


class ExluirTarefaService():
 
    def delete_banco_de_dados(self, id_tarefa):
    
        conn_geral = postgreSQL_pool_geral.getconn()

        cursor = conn_geral.cursor()

        query = f"""
            DELETE FROM lista_tarefas WHERE id_tarefa = '{id_tarefa}'
        """
        cursor.execute(query)

        conn_geral.commit()
        cursor.close()

        postgreSQL_pool_geral.putconn(conn_geral)