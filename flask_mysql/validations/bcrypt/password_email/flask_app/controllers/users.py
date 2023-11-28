from flask_app import app
from flask import request, redirect, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# we are creating an object called bcrypt, 
# which is made by invoking the function Bcrypt with our app as an argument

@app.route('/register/user', methods=['POST'])
def register():
    # validate the form here ...
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # * as we learned earlier, we pass in a string to bcrypts method (generate_password_hash)
    # * which add salt and then hashes to the passed in string.
    
    # * we store it in a variable though so that we can later store
    # * into our data dictiontionary in place of our password.
    # * ^ this is because we cannot request.form the password. that would get us the unsalted/hashed password.
    # * properly is done below
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "username": request.form['username'],
        "email":request.form['email'],
        "password" : pw_hash
    }
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect("/dashboard")



@app.route('/register', methods = ['POST'])
def register():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "username":request.form["username"],
        "email":request.form["email"],
        "password": pw_hash
    }

    user_id = User.save(data)
    session["user_id"] = user_id
    return redirect('/dashboard')

@app.route('/login', methods = ["POST"])
def login():
    user_in_db = User.get_by_email(request.form['email'])
    if not user_in_db:
        flash('invalid email or password')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid email or password')
        return redirect('/')
    session["user_id"] = user_in_db.id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")