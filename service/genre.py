from dao.model.genre import Genre, GenreSchema
from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        return GenreSchema(many=True).dump(self.dao.get_all())

    def get_one(self, gid):
        return GenreSchema().dump(self.dao.get_one(gid))
