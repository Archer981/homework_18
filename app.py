from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    return application


def config_app(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


app = create_app(Config())
config_app(app)


if __name__ == '__main__':
    app.run()
