from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ["POST"])
def process():
    if request.form['which_form'] == 'register':
    # do registration process
        print("register form hidden input")
    elif request.form['which_form'] == 'login':
    # do login process
        print("login form hidden input")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port = 5001)