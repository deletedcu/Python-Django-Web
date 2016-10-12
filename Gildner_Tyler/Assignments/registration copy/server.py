from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = '123456'

@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')


@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("PUT YOUR EMAIL IN THE FUCKING BLANK!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif not request.form['first_name'].isalpha():
        flash('FIX YOUR FIRST NAME!')
    elif not request.form['last_name'].isalpha():
        flash('FIX YOUR LAST NAME!')
    elif request.form['password'] < 8:
        flash('Password length is fucked')
    elif request.form['password'] != request.form['confirm_password']:
        flash('You are definitely making this difficult for yourself, passwords need to match...')
    else:
        flash('Success')

    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']

    return redirect('/')
app.run(debug=True)
