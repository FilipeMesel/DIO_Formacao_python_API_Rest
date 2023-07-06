# Criando uma rest api completa para inclusão de novos desenvolvedores e conhecimentos usando flask-rest
#pip install flask-restful
from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from habilidades import Habilidades
import json

desenvolvedores = [
    {
        'id': 0,
        'nome':'Rafael',
        'habilidades':
        [
            'python',
            'Flask'
        ]
    },
    {
        'id': 1,
        'nome':'Mesel',
        'habilidades':
        [
            'python',
            'Flask'
        ]
    }
]

app = Flask(__name__)
api = Api(app)

class Desenvolvedor(Resource):
    """Devolve um desenvolvedor pelo ID. Também altera e deleta um desenvolvedor 

    Args:
        id (int): identificador único do desenvolvedor na lista

    Returns:
        json: status do retorno
    """
    def get(self, id):
        try:
            response = desenvolvedores[id]
            return response
        except IndexError:
            response = {'status': 'erro', 'code': '{}'.format(IndexError)}
            return response

    def put(self, id):
        try:
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            return dados
        except IndexError:
            response = {'status': 'erro', 'code': '{}'.format(IndexError)}

    def delete(self, id):
        try:
            desenvolvedores.pop(id)
            return 'Excluido'
        except IndexError:
            response = {'status': 'erro', 'code': '{}'.format(IndexError)}
            return response

class listaDesenvolvedores(Resource):
    """Lista todos os desenvolvedores e também inclui um novo desenvolvedor
    """
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
    
    def get(self):
        return desenvolvedores


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(listaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug = True)
