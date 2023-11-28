from flask_app.models import pizza
from flask_app.models import restaurant
from flask_app import app
from flask import render_template, request, redirect

@app.route('/add/pizza')
def add_pizza():
    restaurants = restaurant.Restaurant.get_all()
    return render_template('add_pizza.html', restaurants = restaurants)

@app.route('/save/pizza', methods = ["POST"])
def save_pizza():
    pizza.Pizza.save(request.form)
    return redirect('/existing/pizzas')

@app.route('/existing/pizzas')
def exitsting_pizza():
    pizzas = pizza.Pizza.get_all()
    return render_template('existing_pizzas.html', pizzas = pizzas)

@app.route('/pizza/<pizza_id>')
def selected_pizza(pizza_id):
    selected_pizza = pizza.Pizza.get_one(pizza_id)
    return render_template('selected_pizza.html', pizza = selected_pizza)

@app.route('/pizza/toppings/<pizza_id>')
def get_pizza_with_toppings(pizza_id):
    finished_pizza = pizza.Pizza.get_pizza_with_toppings(pizza_id)
    return render_template('pizza_with_toppings.html', pizza = finished_pizza)
