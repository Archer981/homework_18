from flask_restx import Namespace, Resource
from setup_db import db
from dao.model.movies import Movie, MovieSchema
from conteiner import movie_service


movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return movie_service.get_all()

    def post(self):
        pass


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        pass

    def put(self, mid):
        pass

    def delete(self, mid):
        pass
