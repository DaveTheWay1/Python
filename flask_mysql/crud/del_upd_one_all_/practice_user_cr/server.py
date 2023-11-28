from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods = ["POST"])
def create():
    data = request.form
    User.save(data)
    return redirect('/users')

@app.route('/users')
def show_users():
    users = User.get_all()
    return render_template('show_users.html', users = users)

@app.route('/edit/page/<user_id>')
def edit_user(user_id):
    user = User.get_one(user_id)
    return render_template('edit_page.html', user = user)

@app.route('/update', methods = ["POST"])
def update_user():
    User.update(request.form)
    return redirect(f'/show/user/{request.form["id"]}')

@app.route('/show/user/<user_id>')
def show_user(user_id):
    user = User.get_one(user_id)
    return render_template("show_one_user.html", user = user)

@app.route('/delete/user/<user_id>')
def delete(user_id):
    User.delete(user_id)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True, port = 5001)