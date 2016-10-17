from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'knsdv8unjjasdfionwjnfasdujfin1'
mysql = MySQLConnector(app,'logindb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['pwd']
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = { 'email': email }
    user = mysql.query_db(query, data)
    if bcrypt.check_password_hash(user[0]['pw_hash'],password):
        session['email'] = request.form['email']
        return redirect ('/success')
    else:
        flash('Invalid Username or Password')
        return redirect ('/')

@app.route('/logout')
def logout():
    session.pop('email')
    flash('Logout successful')
    return redirect('/')

@app.route('/registering',methods=['POST'])
def registering():
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email')
        return redirect('/register')
    if len(request.form['first']) < 2:
        flash('Need a First Name')
        return redirect('/register')
    elif not request.form['first'].isalpha():
        flash('No numbers in your name')
        return redirect('/register')
    if len(request.form['last']) < 2:
        flash('Email too short')
        return redirect('/register')
    elif not request.form['last'].isalpha():
        flash('Only letters please')
        return redirect('/register')
    elif len(request.form['pwd']) < 8:
        flash('Password must be at least 8 Characters')
        return redirect('/register')
    elif request.form['pwd'] != request.form['confirm']:
        flash('Password did not Match')
        return redirect('/register')

    pw_hash = bcrypt.generate_password_hash(request.form['pwd'])
    query = "INSERT INTO users (first_name,last_name,email,pw_hash,updated_at,created_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
    data = {
        'first_name':request.form['first'],
        'last_name':request.form['last'],
        'email':request.form['email'],
        'pw_hash':pw_hash
    }
    mysql.query_db(query, data)
    return redirect('/success')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)
