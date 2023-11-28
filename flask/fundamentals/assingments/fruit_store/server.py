from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/purchase', methods=["POST"])
def purhcase():
    print(f"Form: {request.form}")
    print(f"Strawberries: {request.form['strawberry']}")
    print(f"Raspberries: {request.form['raspberry']}")
    print(f"Apples: {request.form['apple']}")
    print(f"Full Name: {request.form['name']}")
    print(f"Student ID: {request.form['id']}")
    return redirect('/checkout')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == "__main__":
    app.run(debug=True, port = 5001)

# * WE WILL COME BACK TO THIS ONCE WE HAVE LEARNED HOW. 
# * THIS ASSIGNEMNT WAS INTENTIONIALLY ALLOWING US TO DO IT THE BROKEN WAY. I DONT WANT THAT.
# * THEY WANTED US TO RENDER A TEMPLATE ON A POST REQUEST