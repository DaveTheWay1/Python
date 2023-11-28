from flask_app.models import user
from flask_app import app
from flask import render_template,request, redirect, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods = ["POST"])
def save_user():
    if not user.User.validate_create(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "first_name":request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password":pw_hash
    }
    user_id = user.User.save(data)
    session["user_id"] = user_id
    return redirect('')

@app.route('/login', methods = ["POST"])
def login():
    data = {"email":request.form["email"]}
    user_id = user.User.getByEmail(data)
    if not user_id:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_id.password, request.form["password"]):
        flash("Invalid Email/Password")
        return redirect('/')
    session["user_id"] = user_id
    return redirect('')

@app.route('/logout')
def logout():
    session.clear
    return redirect('/')