from dao.model.movies import Movie, MovieSchema
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_movies(self, filter_args):
        if not filter_args:
            return MovieSchema(many=True).dump(self.dao.get_all())
        elif filter_args.get('director_id'):
            return MovieSchema(many=True).dump(self.dao.get_movie_by_director(filter_args['director_id']))
        elif filter_args.get('genre_id'):
            return MovieSchema(many=True).dump(self.dao.get_movie_by_genre(filter_args['genre_id']))
        elif filter_args.get('year'):
            return MovieSchema(many=True).dump(self.dao.get_movie_by_year(filter_args['year']))

    def get_one(self, mid):
        return MovieSchema().dump(self.dao.get_one(mid))

    def create(self, data):
        new_record = Movie(**data)
        self.dao.create(new_record)

    def update(self, new_data):
        new_movie = self.dao.get_one(new_data['id'])
        new_movie.title = new_data.get('title', new_movie.title)
        new_movie.description = new_data.get('description', new_movie.description)
        new_movie.trailer = new_data.get('trailer', new_movie.trailer)
        new_movie.year = new_data.get('year', new_movie.year)
        new_movie.rating = new_data.get('rating', new_movie.rating)
        new_movie.genre_id = new_data.get('genre_id', new_movie.genre_id)
        new_movie.director_id = new_data.get('director_id', new_movie.director_id)
        self.dao.update(new_movie)

    def delete(self, mid):
        delete_movie = self.dao.get_one(mid)
        self.dao.delete(delete_movie)
