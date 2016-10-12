from flask import Flask, request, redirect, render_template, session, flash
from flask.ext.bcrypt import Bcrypt
from mysql_connection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = ')()#&$$FHSO*#H)(U#@#!@E)'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login_registration')

def validRegistration():
	if (len(request.form['fname']) < 1 or
	    len(request.form['lname']) < 1 or
	    len(request.form['email']) < 1 or
	    len(request.form['pw']) < 1 or
	    len(request.form['confirm_pw']) < 1):
		flash('All inputs required', 'registration_error')
		return False
	elif (len(request.form['fname']) < 2 or 
	      len(request.form['lname']) < 2):
		flash('First and Last name requires at least 2 characters!', 'registration_error')
		return False
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email address format!', 'registration_error')
		return False
	elif (len(request.form['pw']) < 8 or
		  len(request.form['confirm_pw']) < 8):
		flash('Passwords must be at least 8 characters!', 'registration_error')
		return False
	elif not request.form['pw'] == request.form['confirm_pw']:
		flash('Passwords do not match!', 'registration_error')
		return False
	
	return True
		
def validLogin():
	if (len(request.form['login_email']) < 1 or
	    len(request.form['login_pw']) < 1):
		flash('All inputs required', 'login_error')
		return False
	elif not EMAIL_REGEX.match(request.form['login_email']):
		flash('Invalid email address format!', 'login_error')
		return False
	
	return True
	
@app.route('/')
def login_register():
	return render_template('login_registration.html')

@app.route('/login', methods=['POST'])
def login():
	if not validLogin():
		return redirect('/')
	
	query = 'select * from user where email=:email'
	data = {
		'email': request.form['login_email']
	}
	
	user_data = mysql.query_db(query, data)
	
	if len(user_data) < 1:
		flash('Invalid username, try again or register!', 'login_error')
		return redirect('/')
		
	print('user in database')
	
	# verify login credentials and login user
	if not bcrypt.check_password_hash(user_data[0]['password'], request.form['login_pw']):
		flash('Invalid login credentials, try again!', 'login_error')
		return redirect('/')
		
	if not 'logged_in_userid' in session:
		session['logged_in_userid'] = user_data[0]['id']
		
	return redirect('/home')

@app.route('/register', methods=['POST'])
def register():
	if not validRegistration():
		return redirect('/')
	
	# store user info in db and login user
	query = 'insert into user (first_name, last_name, email, password, created_at, updated_at) values (:first_name, :last_name, :email, :hashed_pw, NOW(), NOW())'
	data = {
		'first_name': request.form['fname'],
		'last_name': request.form['lname'],
		'email': request.form['email'],
		'hashed_pw': bcrypt.generate_password_hash(request.form['pw'])
	}
	
	user_id = mysql.query_db(query, data)
	
	# successful registration
	if not 'logged_in_userid' in session:
		session['logged_in_userid'] = user_id
	
	# redirect then display logged in user's name on index.html
	return redirect('/home')

@app.route('/home')
def go_home():
	# retrieve user name for session['logged_in_userid'] and other necessary info for user
	query = 'select first_name, last_name from user where id=:id'
	data = {
		'id': session['logged_in_userid']
	}
	
	user_data = mysql.query_db(query, data)
	
	if len(user_data) < 1:
		flash('Internal Error...contact support!', 'login_error')
		redirect('/')
		# something critical went wrong, non-registered user still got in!!!
	
	return render_template('index.html', value=user_data[0])
	
@app.route('/logout')
def logout():
	session.clear()
	
	return redirect('/')

app.run(debug=True)