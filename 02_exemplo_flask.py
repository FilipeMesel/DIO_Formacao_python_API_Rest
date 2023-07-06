from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

# Usando Json
@app.route("/")
def pessoa():
    """Rota que retorna um Json com Flask

    Returns:
        Json str: Retorna um json com o nome de uma pessoa
    """
    return jsonify({'nome': 'Mesel', 'Profissao': 'desenvolvedor'})

@app.route("/<int:id>")
def pessoa_retorna_id(id):
    """Rota que retorna um Json com Flask

    Args:
        id: Identificador único de uma pessoa

    Returns:
        Json str: Retorna um json com o nome de uma pessoa
    """
    return jsonify({'id':id, 'nome': 'Mesel', 'Profissao': 'desenvolvedor'})

@app.route("/soma/<int:valor1>/<int:valor2>/")
def soma(valor1, valor2):
    """Soma de dois valores

    Args:
        valor1 (int): valor para somar
        valor2 (int): valor para somar
    
    Returns:
        JSON: Json contendo a soma de dois parâmetros
    
    Test:
        /soma/1/2
        ou
        /soma/1/2/
    """
    return jsonify({'soma': valor1 + valor2})
    
@app.route('/soma', methods=['POST'])
def soma_post():
    """Soma de dois valores passados via POST

    Args:
        valor1 (int): valor para somar
        valor2 (int): valor para somar
    
    Returns:
        JSON: Json contendo a soma de dois parâmetros
    
    Test:
        Faça um post na url
        /soma
        com o body:
        {
            "valor1": 1,
            "valor2": 2
        }
    """
    #Pegando dados do body em formato json
    dados = json.loads(request.data)
    print(dados)
    valor1 = dados['valor1']
    valor2 = dados['valor2']
    return jsonify({'soma': valor1 + valor2})


@app.route('/soma', methods=['POST', 'GET'])
def soma_post_get():
    """Soma de dois valores passados via POST

    Args:
        valor1 (int): valor para somar
        valor2 (int): valor para somar
    
    Returns:
        JSON: Json contendo a soma de dois parâmetros
    
    Test:
        Faça um post na url
        /soma
        com o body:
        {
            "valor1": 1,
            "valor2": 2
        }
    """
    total = 20
    retorno= 0
    if request.method == 'POST':
        #Pegando dados do body em formato json
        dados = json.loads(request.data)
        print(dados)
        valor1 = dados['valor1']
        valor2 = dados['valor2']
        total = valor1 + valor2
        return jsonify({'soma': total})
    elif request.method == 'GET':
        return jsonify({'soma': total})

app.run(debug=True)