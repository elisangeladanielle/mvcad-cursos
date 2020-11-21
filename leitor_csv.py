import csv

#from pessoa_pygres import insere_pessoa, retorna_pessoas
#from psycopg_connection import cursor
from pessoa_psycopg import insere_pessoa, retorna_pessoas

def ler_arquivo():
    with open('curso-mvcad.csv', encoding="utf8") as file:
        leitor = csv.DictReader(file, delimiter=',')

        #pygres
        # pygres_connection.cursor.execute(select * from pessoa)
        # print(pygres_connection.cursor.fetchall())
        #cursor.execute("select relname from pgclass where relkind='r' and relname !~ '^(pg|sql_)';")
        #cursor.execute("select * from pessoa")
        #print(cursor.fetchall())

        #List Comprehention
        # lista_pessoas = [item for item in leitor]
        # print(lista_pessoas)
        #
        # for item in lista_pessoas:
        #   print(item)

#ler_arquivo()

pessoa = {
    'nome': "Lisa",
    'endereco': "Jardim Camargo Novo",
    'cpf': '12345678930',
    'estado': "São Paulo",
    'turma': "MVCAD Python 1",
    'periodo': "matutino",
    'modulo': "MVCAD",
}

insere_pessoa(pessoa)
print(retorna_pessoas())
