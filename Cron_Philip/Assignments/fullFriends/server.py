from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'IgotThisDude!'

mysql = MySQLConnector(app,'fullFriends')

def valid():
    if (len(request.form['email']) < 1 or 
    len(request.form['first_name']) < 1 or 
    len(request.form['last_name']) < 1):
        flash('All input fields required!')
        return False

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return False
    return True

@app.route('/')
def index():

    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)


@app.route('/friends', methods=['POST'])
def create():

    if not valid():
        return redirect('/')

    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"

    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
            }
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': id}
    friends = mysql.query_db(query, data)
    return render_template('friends.html', one_friend=friends[0])


@app.route('/friends/<id>', methods=['POST'])
def update(id):

    if not valid():
        return redirect('/friends/' + id + '/edit')

    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"

    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'id': id
            }
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):

    query = "DELETE FROM friends WHERE id = :id"

    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
