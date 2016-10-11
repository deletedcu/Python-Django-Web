from flask import Flask, request, redirect, render_template, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends')
app.secret_key ='ThisIsSecret'

@app.route('/')
def index():
    all = mysql.query_db('SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, "%b-%d-%Y %l:%i %p") AS created_at FROM friend')
    return render_template('index.html', all = all)

@app.route('/friends', methods = ['POST'])
def create():
        query = ('INSERT INTO friend (first_name, last_name, email, created_at) VALUES ( :first, :last, :email, NOW())')
        data = {
            'first': request.form['first'],
            'last': request.form['last'],
            'email': request.form['email']
        }
        mysql.query_db(query, data)
        return redirect('/')

@app.route('/friends/<id>/edit', methods=['POST'])
def edit(id):
    session['id'] = id
    return render_template('/other.html')

@app.route('/friends/<id>', methods = ['POST'])
def update(id):
    query= ("UPDATE friend SET first_name = :first , last_name =:last, email =:email WHERE id =:id")
    data = {
        'first': request.form['first'],
        'last': request.form['last'],
        'email': request.form['email'],
        'id': session['id']
    }
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = ('DELETE FROM friend WHERE id =:id')
    data = {
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
