from flask import Flask
from flask import render_template
from flask import session
from flask import request
from flask import redirect
from flask import flash

from mysqlconnection import MySQLConnector

import re
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'SSSH'
mysql = MySQLConnector(app, 'emaildb')


@app.route('/')
def index():
	return render_template('emailval.html')

@app.route('/email', methods= ['post'])
def process():
	if not email_regex.match(request.form['email']):
		flash("Invalid Email Address!")
		return redirect('/')
	query = "INSERT INTO email (email, created_at) VALUES (:email, NOW())"
	data = { 
			'email' : request.form['email'] 
			}
	email = mysql.query_db(query, data)

	query = "SELECT * FROM email"
	email = mysql.query_db(query)
	return render_template('/success.html', all_email=email)

@app.route('/success')
def show_user():
	return render_template('success.html')


app.run(debug=True)