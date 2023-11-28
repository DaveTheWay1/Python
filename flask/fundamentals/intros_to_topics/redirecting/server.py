from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it a secret, keep it safe"
# set a secret key for security purposes

@app.route('/')
def index():
    return render_template('index.html')

# * WITHOUT session
# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     # Never render a template on a POST request.
#     # Instead we will redirect to our index route.
#     return redirect('/show')

# * WITH session
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

# * WITHOUT access and BEFORE session
# @app.route("/show")
# def show_user():
#     print("Showing the User Info From the Form")
#     print(request.form)
#     return render_template("show.html")

# * WITH ACCESS and AFTER SESSION
@app.route('/show')
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

if __name__ == "__main__":
    app.run(debug=True, port = 5001)