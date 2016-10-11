  
from flask import Flask, session, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key= "ojenrfiunc358"
mysql = MySQLConnector(app,'frienddb')

@app.route('/')
def index():
   query = "SELECT * FROM friend"
   friends = mysql.query_db(query)
   return render_template('index.html',friends=friends)

@app.route('/friends', methods =['POST'])
def create():
	query = "INSERT INTO friend(first_name, last_name, email, created) VALUES (:first_name, :last_name, :email, NOW())"
	data = {
		'first_name': request.form['first_name'],
		'last_name' : request.form['last_name'],
		'email': request.form['email']
	}
	if len(request.form['first_name'])<1 and len(request.form['last_name'])<1 :
		flash(' You must enter First name and last name.')
		return redirect('/')
	elif request.form['first_name'].isalpha() != True and request.form['last_name'].isalpha() != True:
		flash('No number allowed in first name and last name fields')
		return redirect('/')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('invalid email, please enter a valid email')
		return redirect('/')

	mysql.query_db(query, data)
	flash('One friend has been added')
	return redirect('/')
   

@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT * FROM friend WHERE id = :id"
	data = { "id" :id }
	friends = mysql.query_db(query, data)
	return render_template('edit.html', update_friend = friends[0])
   

@app.route('/friends/<id>', methods = ['POST'])
def update(id):
	query = "UPDATE friend SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id" 
	data = {
		'first_name': request.form['first_name'],
		'last_name' : request.form['last_name'],
		'email': request.form['email'],
		'id' : id
	}
	if len(request.form['first_name'])<1 and len(request.form['last_name'])<1 :
		flash(' You must enter First name and last name.')
		return redirect('/')
	elif request.form['first_name'].isalpha() != True and request.form['last_name'].isalpha() != True:
		flash('No number allowed in first name and last name fields')
		return redirect('/')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('invalid email, please enter a valid email')
		return redirect('/')

	mysql.query_db(query, data)
	flash('One friend has been updated')
	return redirect('/')
  

@app.route ('/friends/<id>/delete', methods = ['POST'])
def destroy(id):
	query ="DELETE FROM friend WHERE id = :id"
	data = {'id' :id}
	mysql.query_db(query, data)
	flash("Your friend has been successfully removed!")
	return redirect('/')
 


app.run(debug = True)