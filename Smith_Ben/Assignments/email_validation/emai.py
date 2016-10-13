from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'emailval')
app.secret_key = 'secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def validation():
	return render_template('validation.html')


@app.route('/emails', methods=['POST'])
def email():
   if not EMAIL_REGEX.match(request.form['buttonbox']):
   	flash('invalid emale')
   	return redirect('/')
   else:
   	flash ('Great Job!');

   query = "INSERT INTO email (email,updated_at,created_at) VALUES (:email,NOW(),NOW())"
   data = {'email':request.form['buttonbox']}
   mysql.query_db(query,data)
   query = "SELECT created_at FROM email"
   query = "SELECT * FROM email"
   email = mysql.query_db(query)
   # if len(request.form['buttonbox']) < 1:
   # 	flash('need a proper emale')


   return render_template('email.html', email = email)

# @app.route('/emails')
# def show(email_id):
# 	query = "SELECT * FROM email WHERE id = :specific_id"
# 	data = {'specific_id': email_id}
# 	emails = mysql.query_db(query, data)
# 	return render_template('email.html', email = email)

@app.route('/delete/<id>')
def delete(id):
	query = "DELETE FROM email WHERE id = :id"
	data = {'id': id}
	mysql.query_db(query, data)
	flash("The email address ID {} has been deleted".format(id))
	query = "SELECT * FROM email"
	email = mysql.query_db(query)
	return render_template('email.html', email = email)







app.run(debug=True)