from flask import Flask, render_template, request, redirect, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = '&@DHDJ^^(%^(^^^G@#$@#!@EDQADSG' 

@app.route('/')
def index():
  return render_template("index.html")

# check all inputs for length > 0 and password > 8 characters
def validLength(form):
    if ((len(form['email'])) < 1 or 
       (len(form['fname'])) < 1 or 
       (len(form['lname'])) < 1 or
       (len(form['pw'])) <= 8 or
       (len(form['confirm_pw'])) < 1):
       return False;

    return True;

# no numbers in name fields
def validNameFields(form):
    if not form['fname'].isalpha() or not form['lname'].isalpha():
        return False

    return True

# check for matching passwords
def matchingPasswordInputs(form):
    if not form['pw'] == form['confirm_pw']:
        return False

    return True

@app.route('/process', methods=['POST'])
def process():
    print(request.form)

    if not validLength(request.form):
        flash('All input fields required and Password must be more than 8 characters!')
        return redirect('/')
    elif not validNameFields(request.form):
        flash('No numbers allowed in name inputs!')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address format!')
        return redirect('/')
    elif not matchingPasswordInputs(request.form):
        flash('Passwords do not match!')
        return redirect('/')
    
    flash("Thanks for submitting your info!")
    return redirect('/')

app.run(debug=True)