from flask import Flask, redirect, render_template, flash, session, request
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'login_registration')
app.secret_key = 'ThisIsSecret'
bcrypt = Bcrypt(app)
email_reg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#this is an excellent assignment to look back on for password encryption, basic login and registration, ect.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    #Below are a list of validations/checks that makes sure that the login forms are proper, first if the first name field has at least 2 characters, is all letters, second: same for last name, third: if the email is in email format, fourth: if the password is at least 8 characters long, fifth: if the confirmaiton matches the password.
    #The check below is a query to return all emails currently in the database. I then used a for loop to check each index or entry to make sure that the email being used to register doesn't alraedy exist in the database, this works, however there are duplicates in the database since I didn't delete them from earlier entries
    #If i wanted to check to make sure the first or last name as a combo was also original, i would just add on to the check and loop.
    if len(request.form['first']) < 2 or request.form['first'].isalpha() == False:
        flash('First name can only have letters and must be filled out')
        return redirect('/')
    if len(request.form['last']) < 2 or request.form['last'].isalpha() == False:
        flash('Last name can only have letters and must be filled out')
        return redirect('/')
    if not email_reg.match(request.form['email']):
        flash('Email must be in the proper example@example.com format')
        return redirect('/')
    if len(request.form['pwd']) < 8:
        flash('Password must at least 8 characters long')
        return redirect('/')
    if request.form['pwd'] != request.form['confirm']:
        flash("Password and Confirmation don't match")
        return redirect('/')
    check = mysql.query_db("SELECT email FROM user")
    for i in check:
        if request.form['email'] == i['email']:
            flash('A user with that email already exists')
            return redirect('/')
    query =('INSERT INTO user (first_name, last_name, email, password, created_at) VALUES (:first, :last, :email, :pwd, NOW())')
    data = {
        'first': request.form['first'],
        'last': request.form['last'],
        'email': request.form['email'],
        'pwd': bcrypt.generate_password_hash(request.form['pwd'])
        #the above line uses bcrypt to encrypt the password and stores the password in that format so I don't have the plain password in the database
    }
    mysql.query_db(query,data)
    #lastly, this query inserts/adds, the new user to the database if it passes all the checks, each check has a return redirect, so if it failed that check, it would take you back to the index page and exit the function
    return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    #the below queries selects all emails, then checks whichever password goes with that email with the one that was entered at log in. This way I can make sure the login in fields actually exist and match a user
    query="SELECT * FROM user WHERE email = :email LIMIT 1"
    data ={ 'email': request.form['login_email']}
    user = mysql.query_db(query, data)
    if bcrypt.check_password_hash(user[0]['password'],request.form['login_pwd']):
        #this uses a bcrypt function to check to make sure the password that matches the email from the database, that was entered in the login field, matches the password entered. The entered password is encrypted since the stored password is encrypted.
        # I use user[0], since even though there should only be one return from the query, it still returns a list of dictionaries, so I'm accessing the first index.
        print 'good'
        return redirect('/success')

    else:
        flash('Login in password or email not correct')
        return redirect('/')

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')
app.run(debug=True)
