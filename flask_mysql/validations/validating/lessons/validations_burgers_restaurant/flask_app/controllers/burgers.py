from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.burger import Burger
from flask_app.models.restaurant import Restaurant

@app.route('/burger')
def burger_index():
    restaurants = Restaurant.get_all()
    return render_template('burger.html', all_restaurants = restaurants)

@app.route('/create/burger', methods = ['POST'])
def create_burger():
    # if there are errors:
    # We call the staticmethod on Burger model to validate
    if not Burger.validate_burger(request.form):
        # * in other words, if Burger.validate_burger(request.form)
        # * doesn't come back as true
        # * redirect to the route where the burger form is rendered.
        return redirect('/')
    # * else no; errors:
    Burger.save(request.form)
    return redirect('/view/burgers')

@app.route('/view/burgers')
def burgers():
    burgers = Burger.get_all()
    restaurants = Restaurant.get_all()
    return render_template('burgers.html', all_burgers = burgers, all_restaurants = restaurants)