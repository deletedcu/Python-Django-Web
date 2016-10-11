from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'athenticate_every_thing_here'
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = 'SELECT * FROM friend'
    friend = mysql.query_db(query)
    return render_template('index.html', all_friends = friend)

@app.route('/friends', methods = ['POST'])
def create_friend():
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Email does not exsist.')
        return redirect('/')
    if not request.form['first_name'].isalpha():
        flash('Please enter your name.')
        return redirect('/')
    if not request.form['last_name'].isalpha():
        flash('Please enter your name.')
        return redirect('/')

    query = 'INSERT INTO friend (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())'

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    mysql.query_db(query, data)

    return redirect('/')

@app.route('/friends/<id>/edit')
def edit_view(id):
    return render_template('edit.html', id = id)


@app.route('/friends/<id>', methods = ['POST'])
def edit(id):
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Email does not exsist.')
        return redirect('/friends/{}/edit'.format(id))
    if not request.form['first_name'].isalpha():
        flash('Please enter your name.')
        return redirect('/friends/{}/edit'.format(id))
    if not request.form['last_name'].isalpha():
        flash('Please enter your name.')
        return redirect('/friends/'+id+'/edit')

    query = "UPDATE friend SET first_name=:first_name, last_name=:last_name, email=:email, created_at=NOW() WHERE id=:id"

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    mysql.query_db(query, data)

    return redirect('/')

@app.route('/friends/<id>/delete', methods = ['POST'])
def delete(id):
    query = "DELETE FROM friend WHERE id = :id"

    data = {
        'id': id
    }

    mysql.query_db(query, data)

    return redirect('/')

app.run(debug=True)
