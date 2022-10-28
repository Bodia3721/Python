from django.db.models import manager

from models.article import Article
from models.author import Author
from models.category import Category
from models.comment import Comment
from models.role import Role
from models.user import User

if __name__ == '__main__':

    user_model = User()
    author_model = Author()
    article_model = Article()
    category_model = Category()
    comment_model = Comment()
    role_model = Role()

    manager.run()