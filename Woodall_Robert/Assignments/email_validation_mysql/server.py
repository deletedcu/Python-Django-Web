from flask import Flask, request, render_template, redirect, flash
from mysql_connection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = ')(*#()F#)(JWEF*WF(*UWEFk))'
mysql = MySQLConnector(app, 'flask_email_validation_mysql')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	if (len(request.form['email']) < 1) or (not EMAIL_REGEX.match(request.form['email'])):
		flash('Invalid email address!', 'error')
		return redirect('/')
	
	# insert data into db
	query = ('insert into user_email (email, created_at, updated_at)'
			 'values (:email, NOW(), NOW())')
	
	data = {
		'email': request.form['email']
	}
	
	mysql.query_db(query, data)
	
	# retrieve all emails and pass to success page
	emails = mysql.query_db('select email, created_at from user_email')
	flash('Valid email address entered...thanks!', 'success')
	
	return render_template('success.html', all_emails=emails)

app.run(debug=True)