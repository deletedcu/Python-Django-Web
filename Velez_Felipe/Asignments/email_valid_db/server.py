from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app, 'emaildb')

@app.route('/')
def index():
	emails = mysql.query_db("SELECT * FROM email")
	print emails
	return render_template("index.html", all_emails = emails)



@app.route('/email', methods = ['POST'])
def process():
	query = "insert into email (email, created_at, updated_at) VALUES(:new_email, NOW(), NOW())"
	data = {
			'new_email' : request.form['email']
	}

	if len(request.form['email']) < 1:		
		flash('Email field is empty')
		return redirect('/')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid Email address')
		return redirect('/')
	

	#add a friend to the database!
	
	mysql.query_db(query, data)
	return redirect('/results')

	#deleting records
@app.route('/results')
def show_emails():
	# flash('Valid email')
	query = "SELECT * FROM email"
	data = mysql.query_db(query)
	return render_template ('results.html', all_emails= data )

@app.route('/success/<email_id>')
def delete_mail(email_id):
	query ="DELETE FROM email WHERE id =:id"
	data = {'id': email_id}
	mysql.query_db(query, data)
	flash('Email has been deleted')
	return redirect('/results')





app.run(debug=True)