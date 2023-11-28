from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.burger import Burger
from flask_app.models.restaurant import Restaurant

@app.route('/')
def restaurant_index():
    return render_template('restaurant.html')

@app.route('/create/restaurant', methods = ['POST'])
def create_restaurant():
    Restaurant.save(request.form)
    return redirect('/burger')

@app.route('/all/restaurants')
def all_restaurants():
    restaurants = Restaurant.get_all()
    return render_template('all_restaurants.html', all_restaurants = restaurants)

@app.route('/restaurant/burgers/<restaurant_id>')
def restaurant_burgers(restaurant_id):
    restaurant = Restaurant.get_restaurant_with_burgers(restaurant_id)
    return render_template('restaurant_burgers.html', restaurant = restaurant)