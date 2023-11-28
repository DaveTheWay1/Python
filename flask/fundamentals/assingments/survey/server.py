from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "squilliam"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form',  methods=["POST"])
def form_submission():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/response')

@app.route('/response')
def response():
    return render_template('response.html', name = session['name'], location = session['location'], language=session['language'], comments = session['comments'] )

if __name__ == "__main__":
    app.run(debug=True, port=5001)