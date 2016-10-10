from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja/')
def display_tmnt():
    return render_template('ninjas.html', filenames = 'tmnt.png')

@app.route('/ninja/<colors>')
def display_ninja(colors):

    img = {
        'blue': 'leonardo.jpg',
        'orange': 'michelangelo.jpg',
        'red': 'raphael.jpg',
        'purple':'donatello.jpg'
    }

    if colors in img:
        return render_template('ninjas.html', filenames = img[colors])

    return render_template('ninjas.html', filenames = 'notapril.jpg')
app.run(debug=True)
