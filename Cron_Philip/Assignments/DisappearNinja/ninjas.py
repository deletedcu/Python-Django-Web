from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    return render_template("ninja.html", filenames="tmnt.png")

@app.route('/ninja/<ninja_color>')
def ninja(ninja_color):
    
    imgs = {
        'blue': 'leonardo.jpg',
        'orange': 'michelangelo.jpg',
        'red': 'raphael.jpg',
        'purple': 'donatello.jpg'
    }

    if ninja_color in imgs:
        return render_template("ninja.html", filenames=imgs[ninja_color])
    return render_template("ninja.html", filenames='notapril.jpg')

app.run(debug=True)
