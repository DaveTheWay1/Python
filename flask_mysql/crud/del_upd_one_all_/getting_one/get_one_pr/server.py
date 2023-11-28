from flask import Flask, request, render_template, redirect
from friend import Friend
app = Flask(__name__)

@app.route("/")
def inedx():
    friends = Friend.get_all()
    return render_template("index.html", all_friends = friends)

# @app.route("/show/friends")
# def friends():
#     friends = Friend.get_all()
#     render_template('/index.html', friends)

@app.route('/create', methods=["POST"])
def index():
    data = {
        "fname":request.form["fname"],
        "lname":request.form["lname"],
        "occ": request.form["occ"]
    }
    Friend.save(data)
    return redirect("/")

@app.route('/show/friend/<friend_id>')
def show(friend_id):
    friend = Friend.get_one(friend_id)
    return render_template('show_friend.html', friend = friend)


if __name__ == "__main__":
    app.run(debug=True, port = 5001)