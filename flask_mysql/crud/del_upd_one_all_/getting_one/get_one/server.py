from flask import Flask, render_template, request, redirect
from friend import Friend
app = Flask(__name__)

@app.route('/')
def index():
    friends = Friend.get_all()
    return render_template('index.html', all_friends = friends)

@app.route('/create', methods=["POST"])
def create():
    data = {
        "frsname": request.form["fname"],
        "lsname": request.form["lname"],
        "occ": request.form["occ"]
    }
    Friend.save(data)
    return redirect('/')

# * 1. from the html the /create is triggered.
# * 2. a dictionary is then created to store the information of the inputs of the form
# * we then run the save function found in the class Friend and pass in the data so the information 
# * can be saved. This completes the save functionality.
# * we complete the route though by giving it a proper return. we do so by redirecting as we never render on a POST!!

@app.route('/friend/show/<int:friend_id>')
def show(friend_id):
    # calling the get_one method and supplying it with the id of the friend we want to get
    friend=Friend.get_one(friend_id)
    return render_template("show_friend.html", friend=friend)

if __name__ == "__main__":
    app.run(debug=True, port=5001)