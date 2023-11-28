from flask_app.models.user import User
from flask import render_template, request, redirect
from flask_app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods = ["POST"])
def create():
    data = request.form
    User.save(data)
    return redirect('/show/users')

@app.route('/show/users')
def display_users():
    users = User.get_all()
    return render_template('users.html', users = users)

@app.route('/edit/page/<user_id>')
def edit(user_id):
    user = User.get_one(user_id)
    return render_template('edit.html', user = user)

@app.route('/update', methods = ["POST"])
def update():
    data = request.form
    User.update(data)
    return redirect(f'/user/info/{request.form["id"]}')

@app.route('/user/info/<user_id>')
def user(user_id):
    user = User.get_one(user_id)
    return render_template('user.html', user = user)

@app.route('/delete/user/<user_id>')
def del_user(user_id):
    User.delete(user_id)
    return redirect('/show/users')