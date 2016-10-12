from flask import Flask, render_template, request, redirect,session,flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
valid = True
@app.route('/')
def main_page():
    return render_template('rf.html')

@app.route('/submit',methods=['POST'])
def submit():
    if (len(request.form['email'] and request.form['first_name'] and request.form['last_name'] and request.form['password']) < 1):
        flash('All fields are required and must not be blank!')
        valid = False
    elif not (EMAIL_REGEX.match(request.form['email'])):
        flash('Email should be a valid email!')
        valid = False
    elif not (NAME_REGEX.match(request.form['first_name'] and request.form['last_name'])):
        flash('First and Last Name cannot contain any numbers!')
        valid = False
    elif len(request.form['password']) < 8:
        flash('Password should be more than 8 characters!')
        valid = False
    elif not (request.form['password'] == request.form['confirmation']):
        flash('Password and Password Confirmation should match!')
        valid = False
    if(valid):
        flash('Success!')
    return redirect('/')
app.run(debug = True)
