from flask_restx import Namespace, Resource
from conteiner import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return director_service.get_all()


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        return director_service.get_one(did)
