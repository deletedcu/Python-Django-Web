from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends_db')
app.secret_key = 'secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)

	return render_template('index.html', all_friends = friends)

@app.route('/friends', methods=['POST'])
def create():

	if not EMAIL_REGEX.match(request.form['email']):
		flash('invalid emale')
		return redirect('/')

	query = 'INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())'

	data = {
		'first_name':request.form['first_name'],
		'last_name':request.form['last_name'],
		'email':request.form['email']
	}
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<id>/edit')
def editing(id):
	query = "SELECT friends.first_name, friends.last_name, friends.email, friends.id FROM friends WHERE friends.id = :id"
	data = { 
		'id' :id
	} 
	friends = mysql.query_db(query, data)
	return render_template('update.html', friends=friends[0])
	
@app.route('/friends/<friend_id>', methods=['POST'])
def theid(friend_id):

	if not EMAIL_REGEX.match(request.form['email']):
		flash('invalid emale')
		return redirect('/')
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id;"

	data = {'first_name':request.form['first_name'], 'last_name':request.form['last_name'], 'email':request.form['email'], "id":friend_id}
	mysql.query_db(query, data)
	
	return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])	
def delete(id):
	query = "DELETE FROM friends WHERE id = :id"
	data = {'id': id}
	mysql.query_db(query, data)
	return redirect('/')



app.run(debug=True)