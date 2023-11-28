from flask_app.models import user
from flask_app import app
from flask import render_template, redirect, request

@app.route('/')
def create_user():
    return render_template('index.html')

@app.route('/save/user', methods = ['POST'])
def save_user():
    if user.User.validate_create(request.form):
        user.User.save(request.form)
        return redirect('/user/validated')
    return redirect('/')

@app.route('/user/validated')
def user_validated():
    users = user.User.get_all()
    return render_template('user_validated.html', users = users)