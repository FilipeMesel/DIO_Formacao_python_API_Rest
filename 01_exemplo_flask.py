from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    """primeira rota hello

    Returns:
        str: Frase "Hello world"
    """
    return "hello world"

@app.route("/", methods = ['POST'])
def hello_psot():
    """primeira rota hello post

    Returns:
        str: Frase "Hello world"
    """
    return "hello world"

@app.route("/", methods = ['GET','POST'])
def hello_get_psot():
    """Em python você pode ter a mesma rota com dois métodos diferentes

    Returns:
        str: Frase "Hello world"
    """
    return "hello world"

@app.route("/<numero>", methods = ['GET','POST'])
def hello_get_psot_com_parametro(numero):
    """Em python você pode ter a mesma rota com dois métodos diferentes

    Parâmetros da rota:
        <numero>: String chamada "numero"
        <int:numero>: Inteiro chamado "numero"

    Returns:
        str: Frase "Hello world?" onde ? = algum número passado como parâmetro
    """
    return "hello world {}".format(numero)



#Forma convencional
app.run()

#Forma com debug...O software restarta sempre que você alterar
#Algo próximo ao nodemon do JavaScript
# app.run(debug=True)