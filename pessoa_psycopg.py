from psycopg_connection import cursor

def insere_pessoa(dados_pessoa):

    cursor.execute("INSERT INTO pessoa (nome, endereco, cpf, estado,"
                   "turma, periodo, modulo)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (
                       dados_pessoa['nome'],
                       dados_pessoa['endereco'],
                       dados_pessoa['cpf'],
                       dados_pessoa['estado'],
                       dados_pessoa['turma'],
                       dados_pessoa['periodo'],
                       dados_pessoa['modulo'],
                   )
                   )


def retorna_pessoas():
    cursor.execute("SELECT * FROM pessoa")
    return cursor.fetchall()

