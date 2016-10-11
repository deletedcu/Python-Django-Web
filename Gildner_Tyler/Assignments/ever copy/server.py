from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = '123456'
mysql = MySQLConnector(app,'mydb')
@app.route('/')

def index():

    return render_template('index.html')

@app.route('/email', methods=['POST'])
def create():
    
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    query = "INSERT INTO email (email, created_at) VALUES (:email, NOW())"
    data = {
             'email': request.form['email'],
           }

    mysql.query_db(query, data)

    query = "SELECT * FROM email"
    email = mysql.query_db(query)

    return render_template('email.html', all_email=email)

app.run(debug=True)
