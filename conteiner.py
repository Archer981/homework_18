from setup_db import db
from dao.movie import MovieDAO
from service.movie import MovieService
from dao.director import DirectorDAO
from service.director import DirectorService
from dao.genre import GenreDAO
from service.genre import GenreService


movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
