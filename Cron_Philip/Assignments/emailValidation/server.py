from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'IgotThisDude!'

mysql = MySQLConnector(app,'emailValidation')

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users=users)

@app.route('/success', methods=['POST'])
def success():

        if len(request.form['email']) < 1:
            flash("Email cannot be blank!")
        elif not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!")
        else:
            flash("The email address you entered is a VALID email address!") #figure out how to display email address.

            session['email'] = request.form['email']

            query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"

            data = {
                'email': request.form['email']
            }

            emails = mysql.query_db('select email, created_at from users')

            mysql.query_db(query, data)
            return render_template('success.html', all_emails=emails) #figure out how to display email and datetime.

        return redirect('/')

@app.route("/delete/<email>")
def delete(email):
    query = "DELETE FROM users WHERE email = :emailplaceholder"
    data = {'emailplaceholder': email}
    mysql.query_db(query, data)
    flash('You successfully deleted your email!')
    emails = mysql.query_db('select email, created_at from users')
    return render_template('success.html', all_emails=emails)

app.run(debug=True)


