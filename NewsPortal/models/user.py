from sqlalchemy import func
from models.comment import Comment
from config import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    register = db.Column(db.DateTime(timezone=True), default=func.now())
    photo = db.Column(db.String(256), nullable=True)
    confirm = db.Column(db.String(3), nullable=False, default='no')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    comments = db.relationship(Comment, backref='user')
