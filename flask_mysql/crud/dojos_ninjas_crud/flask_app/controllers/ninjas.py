from flask_app.models import ninja, dojo
from flask_app import app
from flask import render_template, redirect, request

@app.route('/create/ninja/page')
def create_ninja_page():
    dojos = dojo.Dojo.get_all()
    return render_template('create_ninja.html', dojos = dojos)

@app.route('/ninja/save', methods = ["POST"])
def save_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')
