from flask import request
from flask_restx import Namespace, Resource
from conteiner import movie_service


movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        filter_args = request.args
        return movie_service.get_movies(filter_args)

    def post(self):
        new_record = request.json
        movie_service.create(new_record)
        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        return movie_service.get_one(mid)

    def put(self, mid):
        new_data = request.json
        new_data['id'] = mid
        movie_service.update(new_data)
        return '', 201

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 201
