# Criando uma rest api completa para inclusão de novos desenvolvedores e conhecimentos
from flask import Flask
from flask import jsonify
from flask import request
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

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    """Devolve um desenvolvedor pelo ID. Também altera e deleta um desenvolvedor 

    Args:
        id (int): identificador único do desenvolvedor na lista

    Returns:
        json: status do retorno
    """
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
            return jsonify(response)
        except IndexError:
            response = {'status': 'erro', 'code': '{}'.format(IndexError)}
            return jsonify(response)
    elif request.method == 'PUT':
        try:
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            return jsonify(dados)
        except IndexError:
            response = {'status': 'erro', 'code': '{}'.format(IndexError)}
    elif request.method == 'DELETE':
        try:
            desenvolvedores.pop(id)
            return 'Excluido'
        except IndexError:
            response = {'status': 'erro', 'code': '{}'.format(IndexError)}
            return jsonify(response)

@app.route('/dev/', methods = ['POST', 'GET'])
def lista_desenvolvedores():
    """Lista todos os desenvolvedores e também inclui um novo desenvolvedor
    """
    if request.method == 'GET':
        return jsonify(desenvolvedores)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

if __name__ == '__main__':
    app.run(debug = True)
