from flask import Flask, render_template, request, redirect, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def index():
  return render_template("index.html")

def validLength(form):
    if ((len(form['email'])) < 1 or 
        (len(form['first_name'])) < 1 or 
        (len(form['last_name'])) < 1 or 
        (len(form['password'])) <= 8 or 
        (len(form['confirm_password'])) < 1):
        return False;

    return True;

def validNameFields(form):
    if not form['first_name'].isalpha() or not form['last_name'].isalpha():
        return False;

    return True;
def matchingPasswordInputs(form):
    if not form['password'] == form['confirm_password']:
        return False;

    return True;

@app.route('/process', methods=['POST'])
def process():

    if not validLength(request.form):
        flash('All input fields required!')
        flash('Password must be more than 8 characters!')
        return redirect('/')
    elif not validNameFields(request.form):
        flash('No numbers allowed in name input!')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address!')
        return redirect('/')
    elif not matchingPasswordInputs(request.form):
        flash('Password and Confirm password fields must match!')
        return redirect('/')


    flash('Thanks for submitting your information!')
    return redirect('/')

app.run(debug=True)
