from config import app
import pymysql

from models.article import Article
from models.author import Author
from models.category import Category
from models.comment import Comment
from models.role import Role
from models.user import User

from views.home import HomeController
from views.news import NewsController

if __name__ == '__main__':

    home_controller = HomeController()
    news_controller = NewsController()
    app.run(debug=True)