from flask_restx import Namespace, Resource
from conteiner import genre_service


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return genre_service.get_all()


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        return genre_service.get_one(gid)
