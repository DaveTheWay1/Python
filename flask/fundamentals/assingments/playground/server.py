from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def three_boxes():
    return render_template('index.html')

@app.route('/play/<int:num>')
def num_boxes(num):
    return render_template('num.html', num = num)

@app.route('/play/<int:num>/<color>')
def num_color(num, color):
    return render_template('num_color.html', num = num, color = color)

if __name__ == "__main__":
    app.run(debug=True)
