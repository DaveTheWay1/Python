from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask import render_template, request, redirect

@app.route('/')
def create_dojo_page():
    dojos = Dojo.get_all()
    return render_template('index.html', dojos = dojos)

@app.route('/create/dojo', methods = ["POST"])
def save_dojo():
    Dojo.save(request.form)
    return redirect('/')

@app.route('/dojo/page/<dojo_id>')
def dojo_page(dojo_id):
    dojo = Dojo.get_dojo_with_ninjas(dojo_id)
    return render_template('dojo_page.html', dojo = dojo)