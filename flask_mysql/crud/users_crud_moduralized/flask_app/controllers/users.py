from flask_app import app
from flask import request, redirect, render_template
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods = ["POST"])
def create():
    User.save(request.form)
    return redirect('/show/users')

@app.route('/show/users')
def show_all():
    users = User.get_all()
    return render_template('show_users.html', users = users)

@app.route('/get/user/<user_id>')
def one_user(user_id):
    user = User.get_one(user_id)
    return render_template("one_user.html", user = user)

@app.route('/edit/page/<user_id>')
def edit_page(user_id):
    user = User.get_one(user_id)
    return render_template("edit_page.html", user = user)

@app.route('/update', methods = ["POST"])
def update_user():
    User.update(request.form)
    return redirect(f'/get/user/{request.form["id"]}')

@app.route('/delete/<user_id>')
def delete_user(user_id):
    User.delete(user_id)
    return redirect('/show/users')