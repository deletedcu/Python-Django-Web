from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = 'This'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ninja')
def ninja():
    return render_template('other.html', color = 'tmnt.png')
@app.route('/ninja/<color>')
def dissapear(color):
    if color == 'red':
        var = 'raphael.jpg'
    elif color == 'blue':
        var = 'leonardo.jpg'
    elif color == 'orange':
        var = 'michelangelo.jpg'
    elif color == 'purple':
        var = 'donatello.jpg'
    else:
        var = 'notapril.jpg'
    return render_template('other.html', color = var)


app.run(debug=True)
