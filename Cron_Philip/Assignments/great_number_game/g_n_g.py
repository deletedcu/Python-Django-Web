from flask import Flask, render_template, request, redirect,  session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'number' not in session:
        session['format'] = 'hide'
        session['number'] = random.randrange(0, 101)
        print session['number']
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['answer'] = int(request.form['my_guess'])
    print session['answer']
    print session['answer'] == session['number']
    if session['answer'] == session['number']:
        session['feedback'] = 'You win!'
        session['format'] = 'correct boxStyle'
        session['formatG'] = 'hide'
        session['formatGuess'] = 'show'
        return redirect('/')
    elif session['answer'] < session['number']:
        session['feedback'] = 'Too low!'
        session['format'] = 'guess boxStyle'
        session['formatG'] = 'show'
        session['formatGuess'] = 'hide'
    else:
        session['feedback'] = 'Too high!'
        session['format'] = 'guess boxStyle'
        session['formatG'] = 'show'
        session['formatGuess'] = 'hide'
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)

