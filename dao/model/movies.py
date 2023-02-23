from marshmallow import fields, Schema
from setup_db import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    trailer = db.Column(db.String(100))
    year = db.Column(db.Integer())
    rating = db.Column(db.Float())
    genre_id = db.Column(db.Integer())
    director_id = db.Column(db.Integer())


class MovieSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Float()
    genre_id = fields.Integer()
    director_id = fields.Integer()
