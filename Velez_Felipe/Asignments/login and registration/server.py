from flask import Flask, session, render_template, redirect, flash, request
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# import the Connector function
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "Thisissecret"
mysql = MySQLConnector(app, 'frienddb')

@app.route('/')
def index():
	query = "SELECT * FROM friend"
	login = mysql.query_db(query)
	return render_template('index.html', login=login)

@app.route('/registration', methods = ['POST'])
def registration():
	query ="INSERT INTO friend(first_name, last_name, email, password, created) VALUES(:first_name, :last_name, :email, :password, NOW())"
	data ={
		'first_name' :request.form['first_name'],
		'last_name' :request.form['last_name'],
		'email' :request.form['email'],
		'password' :request.form['password'],
		'pwdconfirm':request.form['pwdconfirm']
	}
	if len(data['first_name'])< 2 or len(data['last_name']) <2:
		flash("First name or last name are empty.")
		return redirect('/')
	elif data['first_name'].isalpha() != True or data['last_name'].isalpha() != True:
		flash('No numbers allowed in first name and last name fields')
		return redirect('/')
	elif not EMAIL_REGEX.match(data['email']):
		flash('Invalid email, please enter a valid email')
		return redirect('/')
	elif len(data['password']) < 8 or len(data['pwdconfirm']) < 8:
		flash('Password must be at least 8 characters long')
		return redirect('/')

	elif not data['password'] == data['pwdconfirm']:
		flash('Password fields do not match')
		return redirect('/')
	data['password'] = bcrypt.generate_password_hash(data['password'])
	mysql.query_db(query, data)
	flash('Congratulations, you are register!!!')
	return redirect('/')


@app.route('/login', methods = ['POST'])
def login():
	data = {
		'email':request.form['email'],
		'password' :request.form['password']
	}
	print data
	user_query = "SELECT * FROM friend WHERE email = :email LIMIT 1"
	
	user = mysql.query_db(user_query, data)
	print user[0]['password']
	if not EMAIL_REGEX.match(data['email']):
		flash('Please enter a valid email')
		return redirect('/')
	elif not bcrypt.check_password_hash(user[0]['password'],data['password']):
		flash('Password and email do not match, please enter the correct password')
		return redirect('/')
	elif not 'uid' in session :
		session['uid'] = user[0]['id']
	return redirect('/home')

@app.route('/home')
def home():
	query = "SELECT * FROM friend where id = :id"
	data ={
		'id' : session['uid']
	}
	user_info = mysql.query_db(query, data)

	return render_template('/home.html', user_info = user_info)

@app.route('/logout')
def logout():
	session.clear
	return redirect('/')



# an example of running a query
app.run(debug=True)