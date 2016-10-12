from flask import Flask, redirect, render_template, flash, session, request
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'login_registration')
app.secret_key = 'ThisIsSecret'
bcrypt = Bcrypt(app)
email_reg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
def validation():
    if 'id' in session:
        return True;
    else:
        return False;


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wall')
def wall():
    if (validation() == False):
        flash('You need to be logged in to access this page')
        return redirect('/')
    all = mysql.query_db('SELECT messages.id id, messages.user_id as user_id, messages.message message, users.first_name first, users.last_name last, DATE_FORMAT(messages.created_at, "%b %d %Y %h:%i %p") date FROM messages JOIN users ON users.id = messages.user_id ORDER BY date DESC')
    comment = mysql.query_db('SELECT comments.comment comment, users.first_name first, users.last_name last, comments.message_id cid, DATE_FORMAT(comments.created_at, "%b %d %Y %h:%i %p") date FROM comments JOIN users ON users.id = comments.user_id ORDER BY date DESC')
    return render_template('wall.html', all = all, comment= comment)

@app.route('/process', methods=['POST'])
def register():
    if request.form['action'] == 'register':
        if len(request.form['first']) < 2 or request.form['first'].isalpha() == False:
            flash('First name can only have letters and must be filled out')
            return redirect('/')
        if len(request.form['last']) < 2 or request.form['last'].isalpha() == False:
            flash('Last name can only have letters and must be filled out')
            return redirect('/')
        if not email_reg.match(request.form['email']):
            flash('Email must be in the proper example@example.com format')
            return redirect('/')
        if len(request.form['pwd']) < 8:
            flash('Password must at least 8 characters long')
            return redirect('/')
        if request.form['pwd'] != request.form['confirm']:
            flash("Password and Confirmation don't match")
            return redirect('/')
        check = mysql.query_db("SELECT email FROM users")
        for i in check:
            if request.form['email'] == i['email']:
                flash('A user with that email already exists')
                return redirect('/')
        query="INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (:first, :last, :email, :password, NOW())"
        data = {
            'first': request.form['first'],
            'last': request.form['last'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['pwd'])
        }
        mysql.query_db(query, data)
        flash('Registration successful, please log in')
        return redirect('/')
    elif request.form['action'] == 'login':
        query = 'SELECT * FROM users WHERE email =:email'
        data = { 'email': request.form['login_email']}
        user = mysql.query_db(query,data)
        if len(user) < 1 or bcrypt.check_password_hash(user[0]['password'],request.form['login_pwd']) == False:
            flash('uh oh')
            return redirect('/')
        else:
            flash ('Login email or password incorrect')
            session['id'] = user[0]['id']
            session['name'] = user[0]['first_name']
            return redirect('/wall')


@app.route('/logout', methods=['POST'])
def out():
    session.clear();
    return redirect('/')

@app.route('/message', methods=['POST'])
def message():
    if request.form['action'] == 'message':
        query='INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :userid)'
        data={
            'message': request.form['message'],
            'userid': session['id']
        }
        mysql.query_db(query,data)
    if request.form['action'] == 'comment':
        query= 'INSERT INTO comments (comment, created_at, updated_at, message_id, user_id) VALUES (:comment, NOW(), NOW(), :mess, :use)'
        print request.form['id']
        data = {
            'comment' : request.form['comment'],
            'mess': request.form['id'],
            'use': request.form['user']
        }
        mysql.query_db(query, data)
    if request.form['action'] == 'delete':
        query = 'DELETE FROM messages WHERE id = :id'
        data = { 'id': request.form['delete']}
        mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)
