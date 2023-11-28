from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, request, redirect


@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template('index.html', dojos = dojos)

@app.route('/create/dojo', methods = ["POST"])
def create():
    Dojo.save(request.form)
    return redirect('/')

@app.route('/dojo/page/<dojo_id>')
def dojo_page(dojo_id):
    dojo = Dojo.get_dojo_with_ninja(dojo_id)
    return render_template('dojo_page.html', dojo = dojo)