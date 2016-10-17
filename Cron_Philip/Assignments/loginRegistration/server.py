from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'WeAreTheChampions!'
bcrypt = Bcrypt(app)

mysql = MySQLConnector(app,'loginRegistration') 

@app.route('/')
def index():
  return render_template("index.html")

def validReg():
    if (len(request.form['email']) < 1 or 
        len(request.form['first_name']) < 1 or 
        len(request.form['last_name']) < 1 or  
        len(request.form['password']) < 1 or 
        len(request.form['confirm_password']) < 1):
        flash('All inputs required', 'regError')
        return False;
    elif (len(request.form['first_name']) < 2 or
             len(request.form['last_name']) < 2):
        flash('Name input fields require at least 2 characters', 'regError')
        return False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Valid Email Format Required', 'regError')
        return False
    elif len(request.form['password']) < 8 or len(request.form['confirm_password']) < 8:
        flash('Passwords must be at least 8 charaters', 'regError')
        return False
    elif not request.form['password'] == request.form['confirm_password']:
        flash('Password and Confirm password fields must match', 'regError')
        return False

    return True

def validLog():

    if (len(request.form['email']) < 1 or len(request.form['password']) < 1):
        flash('All inputs required', 'logError')    
        return False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Valid Email Format Required', 'logError')
        return False

    return True 

@app.route('/login', methods=['POST'])
def login():

    if not validLog():
        return redirect('/')

    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = { 'email': email }

    user = mysql.query_db(query, data)
    if len(user) < 1:
        flash('Not a registered user!' 'logError')
        return redirect('/')

    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        # flash('Thanks for submitting your information!', 'logError')
        #logging in.
        if not 'loggedIn' in session:
            print 'loggingin'
            session['loggedIn'] = user[0]['id']
            return redirect('/success')
        else:
            print 'notloggingin'
    else:
        flash('Email or password conflict!', 'logError')
        return redirect('/')

    return redirect('/')

@app.route('/registration', methods=['POST'])
def registration():

    if not validReg():
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
    data = { 
        'first_name': request.form['first_name'], 
        'last_name': request.form['last_name'], 
        'email': request.form['email'], 
        'pw_hash': pw_hash 
    }

    user_id = mysql.query_db(query, data)

    if not 'loggedIn' in session:
        session['loggedIn'] = user_id

    return redirect('/success')

    mysql.query_db(query, data)

    flash('Thanks for submitting your information!')
    return redirect('/success')

@app.route('/success')
def successLogin():

    query = 'select first_name, last_name from users where id=:id'
    data = {
        'id': session['loggedIn']
    }

    user_data = mysql.query_db(query, data)

    return render_template('success.html', value=user_data[0])

@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')


app.run(debug=True)
