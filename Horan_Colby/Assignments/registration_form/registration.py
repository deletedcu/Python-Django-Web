from flask import Flask
from flask import render_template
from flask import session
from flask import request
from flask import redirect
from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'WHAAAAAAAT'

@app.route('/')
def index():
	return render_template('/registration.html')

@app.route('/process', methods= ['post'])
def process():
	user = {
		'email' : request.form['email'],
		'firstname' : request.form['first'],
		'lastname' : request.form['last'],
		'password' : request.form['password'],
		'confirm' : request.form['confirm']
	}
	session['email'] = request.form['email']
	session['first'] = request.form['first']
	session['last'] = request.form['last']
	session['password'] = request.form['password']
	session['confirm'] = request.form['confirm']

	flag = False
	if len(user['email']) < 1:
		flash("Please enter a valid email address.")
		flag = True
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
		flag = True
	if len(user['firstname']) < 1:
		flash("Please enter your first name.")
		flag = True
	if len(user['lastname']) < 1:
		flash("Please enter your last name.")
		flag = True
	if len(user['password']) < 1:
		flash("Please enter a password.")
		flag = True
	if len(user['confirm']) < 1:
		flash("Please confirm your password.")
		flag = True
	if user['firstname'] == int:
		flash('Please enter a valid first name.')
		flag = True
	if user['lastname'] == int:
		flash('Please enter a valid last name.')
		flag = True
	if user['password'] < 8:
		flash('Password must be at least 8 characters.')
		flag = True
	if not user['password'] == (user['confirm']):
		flash("Passwords don't match")
		flag = True
	if flag:
		flash('Thank you for submitting your information to the machine. The machine thanks you.  Trust the machine.')
	return render_template('win.html')

@app.route('/show')
def show_user():
	return render_template('win.html')

app.run(debug = True)