
from flask_restful import Resource

LISTA_HABILIDADES = ['Python', 'Ruby','Java', 'C++', 'Flask']
class Habilidades(Resource):
    def get(self):
        return LISTA_HABILIDADES
