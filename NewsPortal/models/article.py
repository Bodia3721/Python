from config import db
from sqlalchemy.sql import func
from models.comment import Comment


class Article(db.Model):

    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False, unique=True)
    about = db.Column(db.String(256), nullable=False)
    content = db.Column(db.String(1024), nullable=False)
    image = db.Column(db.String(256), nullable=True)
    publish = db.Column(db.DateTime(timezone=True), default=func.now())
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    comments = db.relationship(Comment, backref='article')
