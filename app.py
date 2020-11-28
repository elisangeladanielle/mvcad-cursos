from flask import Flask, request
from flask_restful import Resource, Api

from pessoa_psycopg import retorna_pessoas, insere_pessoa

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


#declarando endpoint (a barra) = raiz da api -- se colocar a url sem a barra do final, tem que vir o resultado tb
api.add_resource(HelloWorld, "/")
api.add_resource(Pessoa, "/pessoas")

# __variável__ = variável privada
# todo o resto é considerada pública
if __name__ == "__main__":
    app.run(debug=True)

