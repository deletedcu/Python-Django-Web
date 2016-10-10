from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'akjbv8934h89suvhnhkljsf8i3'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

mysql = MySQLConnector(app,'emailsdb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emails', methods=['POST'])
def email():
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email sucka')
        return redirect('/')
    query = "INSERT INTO emails (email,updated_at,created_at) VALUES (:email,NOW(),NOW())"
    data = {'email':request.form['email']}
    mysql.query_db(query,data)
    query = "SELECT * FROM emails"
    email = mysql.query_db(query)


    return render_template('email.html', email = email)

@app.route('/delete/<id>')
def delete(id):
    query = "DELETE FROM emails WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    flash("The email address ID {} has been deleted".format(id))
    query = "SELECT * FROM emails"
    email = mysql.query_db(query)
    return render_template('email.html', email = email)

app.run(debug=True)
