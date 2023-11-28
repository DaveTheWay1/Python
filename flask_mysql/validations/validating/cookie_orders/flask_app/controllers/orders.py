from flask_app.models import order
from flask_app import app
from flask import request, redirect, render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/save/order', methods = ["POST"])
def log_order():
    if not order.Order.validate_order(request.form):
        return redirect('/')
    order.Order.save(request.form)
    return redirect('/all/orders')

@app.route('/all/orders')
def all_orders():
    orders = order.Order.get_all()
    return render_template("all_orders.html", orders = orders)

