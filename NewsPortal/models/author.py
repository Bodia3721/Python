from config import db
from models.article import Article


class Author(db.Model):

    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=True, unique=True)

    articles = db.relationship(Article, backref='author')

