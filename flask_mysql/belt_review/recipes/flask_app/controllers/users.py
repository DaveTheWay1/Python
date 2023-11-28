from flask_app.models import user, recipe
from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ["POST"])
def register():
    if not user.User.validate_create(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "password":pw_hash
    }
    user_id = user.User.save(data)
    session["user_id"] = user_id
    return redirect('/home')

@app.route('/login', methods = ["POST"])
def login():
    data = {"email":request.form["email"]}
    user_id = user.User.getByEmail(data)
    if not user_id:
        flash('Invalid Email or Password', 'LoginErr')
        return redirect('/')
    if not bcrypt.check_password_hash(user_id.password, request.form["password"]):
        flash('Invalid Email or Password', 'LoginErr')
        return redirect('/')
    session["user_id"] = user_id.id
    return redirect('/home')

@app.route('/home')
def home():
    if  "user_id" not in session:
        return redirect('/')
    all_recipes = recipe.Recipe.get_recipe_with_creator()
    return render_template('home.html', current_user = user.User.getById({"id":session["user_id"]}), recipes = all_recipes)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')