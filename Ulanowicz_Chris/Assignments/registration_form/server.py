from flask import Flask, render_template, redirect, request, flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "12345678asdfghjwertyzxcvbn"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def validate():
	valid = 'true'
	print request.form
	if len(request.form['first_name']) < 1:
		flash("First name can't be blank")
		valid='false'
	elif not request.form['first_name'].isalpha():
		flash("First name can't contain any numbers")
		valid='false'
	if len(request.form['last_name']) < 1:
		flash("Last name can't be blank")
		valid='false'
	elif not request.form['last_name'].isalpha():
		flash("Last name can't contain any numbers")
		valid='false'
	if len(request.form['email']) < 1:
		flash("Email can't be blank")
		valid='false'
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Please enter a valid email address")
		valid='false'
	if len(request.form['password']) < 1:
		flash("Password can't be blank")
		valid='false'
	elif len(request.form['password']) < 8:
		flash("Password must be at least 8 characters")
		valid='false'
	elif request.form['password'] != request.form['confirm_password']:
		flash("Password doesn't match")
		valid='false'
	if valid == 'false':
		return redirect('/')
	else:
		flash("You have succesfully registered")
	return redirect('/')

app.run()