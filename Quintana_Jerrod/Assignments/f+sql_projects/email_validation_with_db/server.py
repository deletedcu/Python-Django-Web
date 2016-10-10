from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation')
app.secret_key ='ThisIsSecret'
email_reg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def succes():
    if not email_reg.match(request.form['email']):
        flash('Email is not valid!')
        return redirect('/')
    query = 'INSERT INTO email (address, created_at, updated_at) VALUES (:email, NOW(), NOW())'
    dict = {
        'email': request.form['email']
    }
    mysql.query_db(query,dict)
    all = mysql.query_db("SELECT address, DATE_FORMAT(created_at, '%b %d %Y %h:%i %p') AS created_at FROM email")
    return render_template('success.html',  enter = all)
app.run(debug=True)
