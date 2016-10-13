from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'athenticate_all'
mysql = MySQLConnector(app,'emaildb')

@app.route('/')
def index():
    query = "SELECT email, id, DATE_FORMAT(created_at,'%d/%m/%Y %h:%i %p') as created_at FROM email"
    email = mysql.query_db(query)
    return render_template('index.html', all_email = email)

@app.route('/submit', methods=['POST'])
def submit_email():
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Email does not exsist.')
        return redirect('/')
    else:
        flash(request.form['email']+' email successful!')

    query = "INSERT INTO email (email, created_at) VALUES (:email, NOW())"

    data = {
             'email': request.form['email'],
           }
#IMPORTANT - EXECUTE QUERY
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/delete/<id>')
def delete_email(id):
    query = "DELETE FROM email WHERE id = :id"

    data = {
        "id": id
    }

    mysql.query_db(query,data)
    return redirect('/')

app.run(debug=True)
