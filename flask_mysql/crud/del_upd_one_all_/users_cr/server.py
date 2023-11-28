from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=["POST"])
def create():
    data = {
        "fname":request.form["fname"],
        "lname":request.form["lname"],
        "email":request.form["email"]
    }
    user = User.save(data)
    print(user)
    return redirect('/users')

@app.route('/users')
def show_users():
    users = User.get_all()
    return render_template('users.html', all_users = users)

@app.route('/edit/page/<user_id>')
def edit_page(user_id):
    user = User.get_one(user_id)
    return render_template("edit.html", user = user)

@app.route('/update', methods = ["POST"])
def update():
    data = {
        "fname":request.form["fname"],
        "lname":request.form["lname"],
        "email":request.form["email"],
        "id":request.form["id"]
    }
    User.update(data)
    return redirect(f'/show/user/{request.form["id"]}')


@app.route('/show/user/<user_id>')
def show_user(user_id):
    user = User.get_one(user_id)
    return render_template("show_user.html", user = user)

@app.route('/user/delete/<int:delete_id>')
def delete_user(delete_id):
    User.delete(delete_id)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True, port=5001)