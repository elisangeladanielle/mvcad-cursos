import csv

#from pessoa_pygres import insere_pessoa, retorna_pessoas
#from psycopg_connection import cursor

from pessoa_psycopg import insere_pessoa, retorna_pessoas, retorna_pessoa, atualiza_pessoa, remove_pessoa

def ler_arquivo():
    with open('curso-mvcad.csv', encoding="utf8") as file:
        leitor = csv.DictReader(file, delimiter=',')

        for pessoa in leitor:
            cpf = pessoa['cpf'].replace('.', '')
            pessoa['cpf'] = cpf.replace('-', '')
            insere_pessoa(pessoa)

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
        # final, o que ficou
        # for pessoa in leitor:
        #     cpf = pessoa['cpf'].replace('.', '')
        #     pessoa['cpf'] = cpf.replace('-', '')
        #     #pessoa['cpf'] = re.sub(r"[^8-9]+", '', pessoa['cpf']) -- regex = pra cada item da lista retorna tudo o que tiver entre 0 e 9
        #     #print(pessoa['cpf'])
        #     #print(pessoa)
        #     insere_pessoa(pessoa)

#comentado pq se rodar de novo, reinsere todos os dados do arquivo novamente
#ler_arquivo()

# pessoa = {
#     'nome': "Lisa",
#     'endereco': "Jardim Camargo Novo",
#     'cpf': '12345678930',
#     'uf': "SP",
#     'turma': "MVCAD Python 1",
#     'periodo': "matutino",
#     'modulo': "MVCAD",
# }

#insere_pessoa(pessoa)
#atualiza_pessoa(pessoa)
#remove_pessoa(pessoa)

#print(retorna_pessoas())
