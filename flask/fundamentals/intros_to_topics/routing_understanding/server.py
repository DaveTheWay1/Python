from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<word>')
def say(word):
    return f"Hello {word}!"

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return f"{num * word}"

if __name__=="__main__":
    app.run(debug=True)