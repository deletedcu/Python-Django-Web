from flask import Flask, session, request, redirect, flash, render_template
import re

app = Flask(__name__)
app.secret_key='ThisIsSecret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/user', methods=['POST'])
def user():
    if len(request.form['first']) < 1 or len(request.form['last']) < 1  or len(request.form['email']) < 1 or len(request.form['confirm']) < 1 or len(request.form['pass']) < 1:
        flash('Please enter all information')
        return redirect('/')
    elif request.form['first'].isalpha() != True or request.form['last'].isalpha() != True:
        flash('First name and Last name cannot contain numbers')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
        return redirect('/')
    elif len(request.form['pass']) < 9 or request.form['pass'].islower() == True or request.form['pass'].isalpha == True or request.form['pass'].isdigit == True:
        flash('Password must be longer than 8 characters,  contain one uppercase letter, and one number')
        return redirect('/')
    elif request.form['pass'] != request.form['confirm']:
        flash('Password and Confirmation Password do not match')
        return redirect('/')
    else:
        flash('Thanks for submitting info, good job')
        return redirect('/')


app.run(debug=True)
