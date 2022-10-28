import os

from flask import render_template, request, flash, redirect
from werkzeug.utils import secure_filename

from config import app, db
from models.article import Article
from models.author import Author
from models.category import Category


class NewsController(object):

    @staticmethod
    @app.route('/')
    def news_index():
        return render_template('news/index.html', context={
            'page_title': 'Новини',
            'all_categories': Category.query.all(),
            'all_authors': Author.query.all(),
            'all_articles': Article.query.all()
        })

    @staticmethod
    @app.route('/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'GET':
            return render_template('news/create.html', context={
                'page_title': 'Додати новину',
                'all_categories': Category.query.all(),
                'all_authors': Author.query.all()
            })
        elif request.method == 'POST':
            title = request.form.get('title')
            about = request.form.get('about')
            content = request.form.get('content')
            title = request.form.get('title')
            #
            image = request.files.get('image')
            length = image.content_length
            if length > app.config['MAX_CONTENT_LENGTH']:
                flash('Завантаження файлів більше ніж 10МВ не підтримується!')
            else:
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                #
                category = request.form.get('category')
                author = request.form.get('author')
                #
                new_article = Article(
                    title = title,
                    about = about,
                    content = content,
                    image =filename,
                    category_id = int(category),
                    author_id = int(author)
                )
                db.session.add(new_article)
                db.session.commit()
                flash('Стаття успішно створена')
            return redirect('/')


    @staticmethod
    @app.route('/news/details/<article_id>')
    def details(article_id: int):
        return render_template('news/details.html', context={
            'page_title': 'Перегляд новини',
            'single_article': Article.query.get(article_id)
        })

    @staticmethod
    @app.route('/c_filter/<category_id>')
    def c_filter(category_id: int):
        return render_template('news/filter.html', context={
            'page_title': 'Обрані новини',
            'all_categories': Category.query.all(),
            'all_authors': Author.query.all(),
            'filter_articles': Article.query.filter_by(category_id=category_id).all()
        })

    @staticmethod
    @app.route('/a_filter/<author_id>')
    def a_filter(author_id: int):
        return render_template('news/filter.html', context={
            'page_title': 'Обрані новини',
            'all_categories': Category.query.all(),
            'all_authors': Author.query.all(),
            'filter_articles': Article.query.filter_by(author_id=author_id).all()
        })

