from flask_app import app
from flask_app.models import restaurant
from flask import render_template, redirect, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save/restaurant', methods = ["POST"])
def add_restaurant():
    restaurant.Restaurant.save(request.form)
    return redirect('/existing/restaurants')

@app.route('/existing/restaurants')
def existing_restaurants():
    restaurants = restaurant.Restaurant.get_all()
    return render_template('existing_rests.html', restaurants = restaurants)

@app.route('/restaurant/<restaurant_id>')
def select_restaurant(restaurant_id):
    existing_restaurant = restaurant.Restaurant.get_restaurant_with_pizza(restaurant_id)
    return render_template('pizzas_rest.html', restaurant = existing_restaurant)

