from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'mydb')
@app.route('/')

def index():
    query = "SELECT * FROM email"
    friends = mysql.query_db(query)
    return render_template('index.html', all_email=email)

@app.route('/email', methods=['POST'])
def create():
    query = "INSERT INTO friends (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    data = {
             'email': request.form['email'],
           }
    mysql.query_db(query, data)
    return redirect('/')
@app.route('/email/<email_id>')
def show(friend_id):

    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': email_id}
    friends = mysql.query_db(query, data)
    return render_template('index.html', one_friend=friends[0])

app.run(debug=True)
