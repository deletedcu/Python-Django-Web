from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask (__name__)
app.secret_key = 'kjndieuwh347'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'email')

@app.route('/')
def index():
    email = mysql.query_db('SELECT * FROM email')
    print(email)
    return render_template('index.html')



@app.route('/add', methods = ['POST'])
def add():
    
    query = "INSERT INTO email (email, created_at, updated_at) VALUES(:email, NOW(), NOW())"
    data = {
        'email':request.form['email']
    }
    if len(data['email']) < 1:
        flash('Email field cannot be empty')
        return redirect('/')
    elif not EMAIL_REGEX.match(data['email']):
        flash('Please enter a valid email')
        return redirect('/')

    
    mysql.query_db(query,data)
    
    return redirect('/results')

@app.route('/results')
def results():
    flash('The email address you entered is Valid')
    query = 'SELECT * from email'
    datas= mysql.query_db(query)
    return render_template('results.html', emails=datas)

@app.route('/remove/<email_id>')
def delete(email_id):
    query = "DELETE FROM email WHERE id = :id"
    data = {'id' : email_id}
    mysql.query_db(query, data)
    flash("email has been delete")
    return redirect('/results')

app.run(debug=True)