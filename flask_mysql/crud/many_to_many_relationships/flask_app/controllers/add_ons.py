from flask_app.models import add_on
from flask_app.models import topping
from flask_app.models import pizza
from flask_app import app
from flask import render_template, redirect, request

@app.route('/pizza/add/toppings')
def add_toppings_to_pizza():
    pizzas = pizza.Pizza.get_all()
    toppings = topping.Topping.get_all()
    return render_template('add_toppings_to_pizza.html', pizzas = pizzas, toppings = toppings)

@app.route('/save/pizza/add/ons', methods = ["POST"])
def save_add_ons():
    add_on.AddOns.save(request.form)
    return redirect('/pizza/add/toppings')