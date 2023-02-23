from dao.model.director import Director, DirectorSchema
from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        return DirectorSchema(many=True).dump(self.dao.get_all())

    def get_one(self, did):
        return DirectorSchema().dump(self.dao.get_one(did))
