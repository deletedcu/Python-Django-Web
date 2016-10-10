from flask import Flask, redirect, request, render_template, session, flash
from mysql_connection import MySQLConnector
import datetime, re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = '#H^&JT^*&I*JET^'
mysql = MySQLConnector(app, 'full_friends')

def validForm():
	if (len(request.form['fname']) < 1 or 
	    len(request.form['lname']) < 1 or 
	    len(request.form['email']) < 1):
		flash('All inputs required!', 'error')
		return False;
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email address!', 'error')
		return False;
	
	return True

@app.route('/')
def index():
	friends = mysql.query_db('select * from friend')
	return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	if not validForm():
		return redirect('/')
	
	query = ('insert into friend (first_name, last_name, email, created_at, updated_at)'
			 'values (:first, :last, :email, NOW(), NOW())')
	
	data = {
		'first': request.form['fname'],
		'last': request.form['lname'],
		'email': request.form['email']
	}
	
	mysql.query_db(query, data)
	
	return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	# pre-populate form data with desired user
	query = 'select * from friend where id = :id'
	data = { 'id': id }
	friend = mysql.query_db(query, data)
	
	# TODO: validate friend has data in it
	if friend[0]:
		value = friend[0]
	
	return render_template('edit_friend.html', friendToEdit=value)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	if not validForm():
		return redirect('/friends/' + id + '/edit')
	
	query = 'update friend set first_name=:first, last_name=:last, email=:email where id=:id'
	
	data = {
		'first': request.form['fname'],
		'last': request.form['lname'],
		'email': request.form['email'],
		'id': id
	}
	
	mysql.query_db(query, data)
	
	return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
	query = 'delete from friend where id=:id'
	data = { 'id': id }
	
	mysql.query_db(query, data)
	
	return redirect('/')

app.run(debug=True)