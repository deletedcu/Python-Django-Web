from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods = ['POST'])
def user():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['lang']
    session['comment'] = request.form['comment']
    return render_template('submitted.html')


app.run(debug=True)
