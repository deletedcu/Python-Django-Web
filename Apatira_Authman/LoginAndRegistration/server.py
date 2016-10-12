from flask import Flask, redirect, session, render_template, request, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'loginregistration')
app.secret_key = 'jamesBrown'
nameReg = re.compile(r'.a-z{2, 60}/i')
emailReg = re.compile(r'[^@]+@[^@]+\.[^@]+')

@app.route('/')
def index():
   if not 'name' in session:
      session['name'] = ''
   if not 'email' in session:
      session['email'] = ''
   return render_template('index.html')

@app.route('/process', methods=['POST'])
def submitUser():
   insertUser = "INSERT INTO user (first_name, last_name, email, password, password_confirmation, created_at, updated_at) VALUES (:firstname, :lastname, :email, :password, :password_confirmation, Now(), Now())"
   if len(request.form['first_name']) >= 2:
      fname = request.form['first_name']
      session['name'] = request.form['first_name']
   else:
      flash("Please enter Valid name:")
      return redirect('/')
   if len(request.form['last_name']) >= 2:
      lname = request.form['last_name']
   else:
      flash("Please enter valid name: ")
      return redirect('/')
   if emailReg.match(request.form['email']):
      email = request.form['email']
   else:
      flash("Please enter valid email:")
      return redirect('/')
   passw = request.form['password']
   confirm = request.form['confirm']
   if not passw == confirm:
      flash("Fix your passwords:")
      redirect('/')
   pw_hash = bcrypt.generate_password_hash(passw)
   dataCheck = {
		'firstname' : fname,
		'lastname'	: lname,
		'email'	: email,
		'password' : pw_hash,
		'password_confirmation' : pw_hash
	}

   result = mysql.query_db(insertUser, dataCheck)
   print dataCheck
   return redirect('/result')

@app.route('/result')
def pageLoad():
    return render_template('result.html', name = session['name'])


@app.route('/getuser', methods=['POST'])
def login():
    select = "SELECT first_name, last_name, password FROM user WHERE email = :email"
    dataCheck = {
        'email' : request.form['email']
        }
    password = request.form['password']
    user = mysql.query_db(select, dataCheck)
    if bcrypt.check_password_hash(user[0]['password'], password):
        session['email'] = request.form['email']
        print user
        return redirect('/login')
    else:
        flash("User Not found")
        return redirect('/')

@app.route('/login')
def loginPage():
    select = "SELECT first_name, last_name FROM user WHERE email = :email"
    e = {
        'email' : session['email']
        }
    user = mysql.query_db(select, e)
    print user
    return render_template('login.html', name = user[0]['first_name'])

app.run(debug=True)