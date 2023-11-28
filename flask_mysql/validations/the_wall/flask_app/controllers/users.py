from flask_app.models import user
from flask_app.models import post
from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register():
    if user.User.validate_create(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email":request.form["email"],
            "password":pw_hash
        }
        user_id = user.User.save(data)
        session["user_id"] = user_id
        return redirect('/home')
    return redirect('/')

@app.route('/login')
def login():
    data = {"email": request.form["email"]}
    if not user.User.get_by_email(data):
        flash('Invalid email or password')
        return redirect('/')
    user_id = user.User.get_by_email(data)
    if not bcrypt.check_password_hash(user_id.password, request.form["password"]):
        flash('Invalid email or password')
        return redirect('/')
    session["user_id"] = user_id.id
    return redirect('/home')

@app.route('/home')
def dashboard():
    if not "user_id" in session:
        return redirect('/')
    current_user = user.User.get_by_id({"id":session["user_id"]})
    all_posts = post.Post.get_all()
    created_post = post.Post.get_post_with_author()
    detailed_post = post.Post.get_post_with_author()
    return render_template('home.html', current_user = current_user, post_creator = created_post, all_posts = all_posts, detailed_post = detailed_post)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')