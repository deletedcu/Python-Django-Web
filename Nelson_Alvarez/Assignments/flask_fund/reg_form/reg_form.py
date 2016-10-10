from flask import Flask, render_template, request, redirect, session, flash
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'Thisissecret'

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif not request.form['first_name'].isalpha():
        flash('WHATS YOUR FIRST NAME DUMMY?!')
    elif not request.form['last_name'].isalpha():
        flash('DO YOU EVEN HAVE A LAST NAME? Fill IT IN!!!')
    elif request.form['password'] <8:
    	flash('Password length is all WRONG!')
    elif request.form['password'] != request.form['confirm_password']:
    	flash('OHMERGED MATCH YOUR DAMN PASSWORD!!!')

    else:
    	flash('Success')

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']
    
    return redirect('/')

app.run(debug=True)