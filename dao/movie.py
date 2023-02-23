from dao.model.movies import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_movie_by_director(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_movie_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_movie_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, data):
        with self.session.begin():
            self.session.add(data)
            self.session.commit()

    def update(self, data):
        self.session.add(data)
        self.session.commit()

    def delete(self, delete_movie):
        self.session.delete(delete_movie)
        self.session.commit()
