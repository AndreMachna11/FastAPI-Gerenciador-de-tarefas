from BancoDeDados.poolDeConexoes import postgreSQL_pool_geral

class CriaOuAtualizaTarefaService():

    def upsert_banco_de_dados(self, id_tarefa, titulo, descricao, status):
    
        conn_geral = postgreSQL_pool_geral.getconn()

        cursor = conn_geral.cursor()

        query = f"""
            INSERT INTO lista_tarefas (id_tarefa, titulo, descricao, status) 
            VALUES ('{id_tarefa}', '{titulo}', '{descricao}', '{status}')
            ON CONFLICT (id_tarefa) 
            DO UPDATE SET titulo = '{titulo}', descricao = '{descricao}', status = '{status}';
        """

        cursor.execute(query)

        conn_geral.commit()
        cursor.close()

        postgreSQL_pool_geral.putconn(conn_geral)
    
    

    