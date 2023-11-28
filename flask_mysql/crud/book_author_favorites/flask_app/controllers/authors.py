from flask_app.models import author
from flask_app.models import book
from flask_app import app
from flask import render_template, redirect, request

@app.route('/add/author')
def index():
    authors = author.Author.get_all()
    return render_template('add_author.html', authors = authors)

@app.route('/save/author', methods = ["POST"])
def save_author():
    author.Author.save(request.form)
    return redirect('/add/author')

@app.route('/author/<author_id>')
def seleted_author(author_id):
    books =  book.Book.get_all()
    seleted_author = author.Author.get_author_with_favorites(author_id)
    return render_template('author.html', author = seleted_author, books = books)