from flask import render_template
from config import app


class HomeController(object):

    @staticmethod
    @app.route('/main')
    def index():
        return render_template('home/index.html', context={
            'page_title': 'Головна'
        })

    @staticmethod
    @app.route('/about')
    def about():
        return render_template('home/about.html', context={
            'page_title': 'Про сайт'
        })

    @staticmethod
    @app.route('/contact')
    def contact():
        return render_template('home/contact.html', context={
            'page_title': 'Контакти'
        })

    @staticmethod
    @app.route('/feedback')
    def feedback():
        return render_template('home/feedback.html', context={
            'page_title': 'Feedback'
        })