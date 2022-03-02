import email
from enum import unique
import models
from models import Users
from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    movieID = db.Column(db.String(80), unique=True, nullable=False)
    movieRating = db.Column(db.String(120), unique=True, nullable=False)
    comments = db.Column(db.String(120), unique=True, nullable=False)


def __repr__(self):
    return "<Users %r>" % self.username
