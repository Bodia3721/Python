from sqlalchemy import func

from config import db


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(512), nullable=False)
    publish = db.Column(db.DateTime(timezone=True), default=func.now())
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))