
from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
import re
mysql = MySQLConnector(app,'full_friends')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key = "ThisIsSecret!"


@app.route('/')
def index():
    if not 'class' in session:
        session['class'] = ''
    query = "SELECT * FROM friend"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    if len(request.form['first_name']) <1:
        flash('Enter First Name.')
        session['class'] = 'red'
    elif len(request.form['last_name']) <1:
        flash('Enter Last Name.')
        session['class'] = 'red'

    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address.')
        session['class'] = 'red'

    else:
        print request.form['first_name']
        print request.form['last_name']
        print request.form['email']

        query = "INSERT INTO friend (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        data = {
                'first_name': request.form['first_name'],'last_name': request.form['last_name'], 'email': request.form['email']
               }
        mysql.query_db(query,data)

        flash('Your friend ({}) has been added!  Thank you!'.format(request.form['first_name']))
        session['class'] = 'green'

    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friend WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    flash('Your friend has been deleted.')
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM friend WHERE id=:id"
    data = {
            'id': id
           }
    specific_friend = mysql.query_db(query,data)
    return render_template('friends.html', specific_friend = specific_friend[0])

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    if len(request.form['first_name']) <1:
        flash('Enter First Name.')
        session['class'] = 'red'
        return redirect('/friends/'+id+'/edit')
    elif len(request.form['last_name']) <1:
        flash('Enter Last Name.')
        session['class'] = 'red'
        return redirect('/friends/'+id+'/edit')

    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address.')
        session['class'] = 'red'
        return redirect('/friends/{}/edit'.format(id))

    else:
        query = "UPDATE friend SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
        data = {
                'first_name': request.form['first_name'],'last_name': request.form['last_name'], 'email': request.form['email'], 'id': id
               }
        mysql.query_db(query,data)
        flash('Friend updated Successfully')

    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)
