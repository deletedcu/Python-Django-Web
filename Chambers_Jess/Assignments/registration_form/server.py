
from flask import Flask, render_template, redirect, request, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    if not request.form['first_name'].isalpha():
        flash('Invalid First Name')

    elif not request.form['last_name'].isalpha():
        flash('Invalid Last Name')

    elif len(request.form['email']) < 1:
        flash("Email please.")

    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address')

    elif len(request.form['password']) < 8:
        flash('Password must be 8 characters')

    elif request.form['password'] != request.form['password_confirm']:
        flash('Passwords must match.')

    else:
        flash("Success!")

    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['password_confirm'] = request.form['password_confirm']

    return redirect('/')

app.run(debug=True)
