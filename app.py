from flask import Flask, request
from flask_restful import Resource, Api

from pessoa_psycopg import retorna_pessoas, insere_pessoa, retorna_pessoa, remove_pessoa, atualiza_pessoa

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return "Uhuuuul"

class Pessoa(Resource):
    def get(self):
        pessoas = retorna_pessoas()
        return pessoas

    def post(self):
        pessoa = request.json
        insere_pessoa(pessoa)
        return "Pessoa inserida com sucesso!"

# se fosse o patch atualizaria só o parâmetro escolhido, no código é diferente tb
    def put(self):
        pessoa = request.json
        atualiza_pessoa(pessoa)
        return "Pessoa atualizada com sucesso!"


class PessoaDetail(Resource):
    def get(self, id):
        pessoa = retorna_pessoa(id)
        return pessoa

    def delete(self, id):
        remove_pessoa(id)
        return "Pessoa removida com sucesso!"


#declarando endpoint (a barra) = raiz da api -- se colocar a url sem a barra do final, tem que vir o resultado tb
api.add_resource(HelloWorld, "/")
api.add_resource(Pessoa, "/pessoas")
api.add_resource(PessoaDetail, "/pessoa/<int:id>")

# __variável__ = variável privada
# todo o resto é considerada pública
if __name__ == "__main__":
    app.run(debug=True)

