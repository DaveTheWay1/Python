from flask_app.models import topping
from flask_app import app
from flask import render_template, redirect, request

@app.route('/create/topping')
def create_topping():
    return render_template('create_topping.html')

@app.route('/save/topping', methods = ["POST"])
def save_topping():
    topping.Topping.save(request.form)
    return redirect('/create/topping')