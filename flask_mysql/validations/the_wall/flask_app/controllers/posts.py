from flask_app.models import post
from flask_app import app
from flask import redirect, render_template, request, session

@app.route('/create/post', methods = ["POST"])
def create_post():
    if not "user_id" in session:
        return redirect('/')
    if not post.Post.validate_post(request.form):
        return redirect('/home') # redirects to the home page with the flash errors
    data = {
        "content":request.form["content"],
        "user_id":session["user_id"]
    }
    post.Post.save(data)
    return redirect('/home') # redirects to the home page succesfully

