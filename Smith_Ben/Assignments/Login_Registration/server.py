from flask import Flask, redirect, request, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'logindb')
app.secret_key = 'secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
	# email = request.form['regemail']
	# password = request.form['regpwd']
	# query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	# data = { 'email': email }
	# user = mysql.query_db(query, data)
	# if bcrypt.check_password_hash(user[0][pw_hash], password):
	# 	return redirect ('/success')
	# else:
	# 	flash('Invalid Username or Password')
	# 	return redirect ('/')

	return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
	email = request.form['regemail']
	password = request.form['regpwd']
	query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	data = { 'email': email }
	user = mysql.query_db(query, data)
	if bcrypt.check_password_hash(user[0]['pw_hash'], password):
		session['regemail'] = request.form['regemail']
		return redirect ('/success')
	else:
		flash('Invalid Username or Password')
		return redirect ('/')

@app.route('/session')
def sessions():
	return render_template('session.html')

@app.route('/logout')
def logout():
	session.pop('regemail')
	return redirect('/')


@app.route('/registering', methods=['POST'])
def registering():
	if not EMAIL_REGEX.match(request.form['regemail']):
		flash('Invalid E-Male')
		return redirect('/register')
	if len(request.form['regfname']) < 2:
		flash('Need a First Name')
		return redirect('/register')
	elif not request.form['regfname'].isalpha():
		flash('You have numbers in your name? Weirdo')
		return redirect('/register')
	if len(request.form['reglname']) < 2:
		flash('Too short. Story of your life?')
		return redirect('/register')
	elif not request.form['reglname'].isalpha():
		flash('Only letters please')
		return redirect('/register')
	elif len(request.form['regpwd']) < 8:
		flash('Must be at least 8 Characters')
		return redirect('/register')
	elif request.form['regpwd'] != request.form['regcpwd']:
		flash('Password did not Match')
		return redirect('/register')

	pw_hash = bcrypt.generate_password_hash(request.form['regpwd'])

	query = 'INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())'

	data = {
		'first_name':request.form['regfname'],
		'last_name':request.form['reglname'],
		'email':request.form['regemail'],
		'pw_hash': pw_hash
	}
	mysql.query_db(query, data)
	return redirect('/success')

@app.route('/register')
def register():
	return	render_template('register.html')	

@app.route('/success')
def success():

	return render_template('success.html')


app.run(debug=True)
