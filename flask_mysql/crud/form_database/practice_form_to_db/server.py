from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from friend import Friend

@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template('index.html', all_friends = friends)

# * we create a variable call friends which then reaches to our class Friend
# * and runs it's get_all function
# * we print the variable friends which would be all friends found 
# * upon completeing the above lines, we render the template index.html
# * and we pass in friends as we save it in the variable all_friends
# * now, all_friends variable can be implemented into our rendered_template
# * and used to refer to our friends which runs the function that contains all
# * our found friends 

@app.route('/create_friend', methods=["POST"])
def create_friend():
    data = {
        "fname":request.form["fname"],
        "lname": request.form["lname"],
        "occ": request.form["occ"]
    }
    Friend.save(data)
    return redirect("/")

# * we create our route to save a created friend.
# * route is also a methods post retrieving information
# * we create a diction which contain all keys storing an answer from
# * the form retrived using request.form
# * we then reach to our Friend class to then call the save method within it
# * and pass in data,



if __name__ == "__main__":
    app.run(debug=True, port = 5001)