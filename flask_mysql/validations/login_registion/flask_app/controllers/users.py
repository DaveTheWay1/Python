from flask_app.models import user
from flask import flash, render_template, request, redirect, session
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ["POST"])
def login():
    data = { "email" : request.form["email"]}
    user_in_data = user.User.get_by_email(data)
    if not user_in_data:
        flash('Invalid email or password')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_data.password, request.form["password"]):
        flash('Invalid email or password')
        return redirect('/')
    session["user_id"] = user_in_data.id
    return redirect('/dashboard')

@app.route('/register', methods = ["POST"])
def register():
    if not user.User.validate_create(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "username": request.form["username"],
        "email": request.form["email"],
        "password": pw_hash
    }
    user_id = user.User.save(data)

    session["user_id"] = user_id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if "user_id" in session:
        current_user = user.User.get_by_id({"id": session["user_id"]})
        return render_template('dashboard.html', current_user = current_user)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
