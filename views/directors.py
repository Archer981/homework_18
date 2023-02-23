from flask_restx import Namespace, Resource

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        pass


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        pass
