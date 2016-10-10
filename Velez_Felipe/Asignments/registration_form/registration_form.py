from flask import Flask, render_template, request, redirect, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def index():
    return render_template("index.html")

def checkvalidlength(form):
    if ((len(form['email'])) < 1 or
        (len(form['first_name'])) < 1 or
        (len(form['last_name'])) < 1 or
        (len(form['password'])) <= 8 or
        (len(form['confirm_password'])) < 1):
        return False;
    return True;

def validnamefield(form):
    if not form['first_name'].isalpha() or not form['last_name'].isalpha():
        return False
    return True

def matchpasswords(form):
    if not form['password'] == form['confirm_password']:
        return False
    return True


@app.route('/process', methods=['POST'])
def process():
    if not checkvalidlength(request.form):
        flash('all input fields required!')
        flash('Password must be at least 8 characters')
        return redirect('/')
    elif not validnamefield(request.form):
        flash('Not numbers allowed in name fields')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email address')
        return redirect('/')
    elif not matchpasswords(request.form):
        flash('Passwords do not match')
        return redirect('/')


    flash("thanks for submitting your info")
    return redirect('/')

app.run(debug=True)


