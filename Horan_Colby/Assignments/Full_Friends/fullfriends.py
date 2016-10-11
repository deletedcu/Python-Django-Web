from flask import Flask
from flask import render_template
from flask import session
from flask import request
from flask import redirect
from flask import flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "Yessir"

mysql = MySQLConnector(app, 'frands')

@app.route('/') 
def index():   
	query = "SELECT * FROM friend"
	friend = mysql.query_db(query)  
	return render_template('index.html',  all_friends=friend)

@app.route('/friends', methods=['post'])
def create():
	friend = {
			'first_name' : request.form['first_name'],
			'last_name' : request.form['last_name'],
			'email'	: request.form['email']
			}

	query = "INSERT INTO friend (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
	insert = mysql.query_db(query, friend)	
	return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	session['id'] = id
	return render_template('edit.html')

@app.route('/friends/<id>', methods=['post'])
def update(id):
	session['id'] = id
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['email'] = request.form['email']
	query = "UPDATE friend set first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
	friend = {
			'id' : session['id'],
			'first_name' : request.form['first_name'],
			'last_name' : request.form['last_name'],
			'email'	: request.form['email']
			}
	mysql.query_db(query, friend)
	return redirect('/')

@app.route('/friends/<id>/delete', methods = ['post'])
def destroy(id):
	query = "DELETE FROM friend WHERE id = :id"
	friend = {
			'id' : id
			}
	mysql.query_db(query, friend)
	return redirect('/')


app.run(debug = True)