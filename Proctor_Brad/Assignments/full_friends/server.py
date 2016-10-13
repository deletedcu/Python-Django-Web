from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)

app.secret_key = 'q984yunjgljksn09fnkvs'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'fullfriendsdb')

@app.route('/')
def index():
    query = 'SELECT * FROM friends'
    friends = mysql.query_db(query)
    return render_template('index.html',friends = friends)

@app.route('/friends',methods=['POST'])
def create():
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Enter a valid email Sucka!')
        return redirect('/')
    
    query = "INSERT INTO friends (first_name,last_name,email,updated_at,created_at) VALUES (:first_name,:last_name,:email,NOW(),NOW())"
    data = {'first_name':request.form['first_name'],'last_name':request.form['last_name'],'email':request.form['email']}
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    query = 'SELECT friends.first_name,friends.last_name,friends.email,friends.id FROM friends WHERE id = :id'
    data = {'id':id}
    friends = mysql.query_db(query,data)
    return render_template('update.html', friends=friends[0])

@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
    data = {'first_name':request.form['first_name'],'last_name':request.form['last_name'],'email':request.form['email'],'id':friend_id}
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/friends/<id>/delete',methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
