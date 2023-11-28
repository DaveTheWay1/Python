from flask_app.models import favorite
from flask_app import app
from flask import request, redirect

@app.route('/save/favorites', methods = ["POST"])
def save_favorites():
    favorite.Favorite.save(request.form)
    return redirect(f'/book/{request.form["book_id"]}')

@app.route('/author/save/favorites', methods = ["POST"])
def author_save_favorites():
    favorite.Favorite.save(request.form)
    return redirect(f'/author/{request.form["author_id"]}')