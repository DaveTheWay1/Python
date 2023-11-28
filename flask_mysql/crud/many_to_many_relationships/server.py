from flask_app import app

from flask_app.controllers import restaurants, pizzas, toppings, add_ons

if __name__ == "__main__":
    app.run(debug=True, port = 5001)