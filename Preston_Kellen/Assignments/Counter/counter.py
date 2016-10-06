from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
counter = 0

@app.route('/')
def index():
    session['counter'] += 1
    return render_template('counter.html')

@app.route('/hacker')
def hacker():
    session['counter'] = 0
    return redirect('/')

@app.route('/ninja')
def ninja():
    session['counter'] += 1
    return redirect('/')

app.run(debug=True)
