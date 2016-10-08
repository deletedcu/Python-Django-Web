from flask import Flask, render_template, request, redirect, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'irtndvieurnviur'

@app.route('/')
def index():
    return render_template("index.html")
#check all for empty and password >=8
def checkForValuelength(form):
    if ((len(form['email']))< 1 or
        (len(form['fname']))< 1 or
        (len(form['lname']))< 1 or
        (len(form['password']))<=8 or
        (len(form['cpassword']))<= 8):
        return False
    return True
# check for valid name and last name
def validNamefileds(form):
    if not form['fname'].isalpha() or not form['lname'].isalpha():
        return False
    return True
# invalid EMAIL
def matchPassword(form):
    if not form['password'] == form['cpassword']:
        return False
    return True

@app.route('/process', methods=['POST'])
def form_page():
    if not checkForValuelength(request.form):
        flash("All fileds are required and password must be 8 or more characater")
        return redirect('/')

    elif not validNamefileds(request.form):
        flash("Name and last name must not contain numbers")
        return redirect('/')

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email address")
        return redirect('/')
    elif not matchPassword(request.form):
        flash("Password do not match")
        return redirect ('/')

    flash("Form sccessfully submitted")
    return redirect('/')

@app.route('/')
def result_page():
    return redirect('/')

app.run(debug=True)
