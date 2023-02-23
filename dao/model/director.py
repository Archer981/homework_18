from marshmallow import fields, Schema
from setup_db import db


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))


class DirectorSchema(Schema):
    id = fields.Integer()
    name = fields.String()