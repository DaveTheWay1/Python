from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app
from flask import request, render_template, redirect

@app.route('/create/ninja/page')
def create_ninja_page():
    dojos = Dojo.get_all()
    return render_template('create_ninja_page.html', dojos = dojos)

@app.route('/save/ninja', methods = ["POST"])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/saved')

@app.route('/saved')
def saved_confirmation():
    return render_template('saved.html')

@app.route('/edit/ninja/<ninja_id>')
def edit_page(ninja_id):
    ninja = Ninja.get_one(ninja_id)
    dojos = Dojo.get_all()
    return render_template('ninja_edit.html', ninja = ninja, dojos = dojos)

@app.route('/save/update', methods = ["POST"])
def save_update():
    Ninja.update(request.form)
    return redirect(f'/ninja/{request.form["id"]}')

@app.route('/ninja/<ninja_id>')
def show_ninja(ninja_id):
    ninja = Ninja.get_one(ninja_id)
    return render_template('show_ninja.html', ninja = ninja)

@app.route('/ninja/dojo/<dojo_id>')
def view_ninja_dojo(dojo_id):
    dojo = Dojo.get_dojo_with_ninjas(dojo_id)
    return render_template('dojo_page.html', dojo = dojo)

@app.route('/delete/<ninja_id>')
def delete_ninja(ninja_id):
    Ninja.delete(ninja_id)
    return redirect('/')