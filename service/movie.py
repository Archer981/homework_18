from dao.model.movies import MovieSchema
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return MovieSchema(many=True).dump(self.dao.get_all())

    def get_one(self, mid):
        pass

    def create(self, data):
        pass

    def update(self, data):
        pass

    def delete(self, mid):
        pass
