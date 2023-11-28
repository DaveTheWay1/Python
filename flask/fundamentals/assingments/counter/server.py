from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "silence, i keal you"

@app.route('/')
def welcome():
    if 'count' not in session:
        session['count'] = 0
    return render_template('index.html')

@app.route('/count')
def count():
    session['count'] += 1
    return redirect('/')

@app.route('/double')
def you_know_i_had_to_double_it():
    if 'count' in session:
        session['count'] += 2
    return redirect('/')

@app.route('/fine', methods=["POST"])
def increment():
    session['count']+= int(request.form['num'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port = 5001)