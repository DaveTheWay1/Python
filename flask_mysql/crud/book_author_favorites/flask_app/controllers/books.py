from flask_app.models import book
from flask_app.models import author
from flask import render_template, redirect, request
from flask_app import app

@app.route('/add/book')
def add_book():
    books = book.Book.get_all()
    return render_template('add_book.html', books = books)

@app.route('/save/book', methods = ["POST"])
def save_book():
    book.Book.save(request.form)
    return redirect('/add/book')

@app.route('/book/<book_id>')
def selected_at(book_id):
    authors = author.Author.get_all()
    selected_book = book.Book.get_book_with_favorites(book_id)
    return render_template('book.html', book = selected_book, authors = authors)