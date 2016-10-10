from flask import Flask, render_template, redirect, request, session, flash
import re
from time import gmtime, strftime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
PSW_REGEX=re.compile(r'(?=.*?[A-Z])(?=.*?[0-9])')


@app.route('/')
def index():
  if 'first_name' not in session:
    session['first_name']=""
  if 'last_name' not in session:
    session['last_name']=""
  if 'email' not in session:
    session['email']= ""
  if 'bday' not in session:
    session['bday']= str(strftime("%Y-%m-%d", gmtime()))
  print session['bday']
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
  verify=True
  session['first_name'] = request.form['first_name']
  session['last_name'] = request.form['last_name']
  session['email'] = request.form['email']
  session['bday'] = request.form['bday']

  if len(session['first_name']) < 1 or len(session['last_name']) < 1:
    flash("Name (First and Last)", "error_type1")
    verify=False
  elif session['first_name'].isalpha() == False or session['last_name'].isalpha() == False:
    flash("Name (First or Last) can only contain letters!", "error_type2")
    verify=False

  if session['bday'] >= str(strftime("%Y-%m-%d", gmtime())):
    flash("You must be at least a day old to register! Please check your birthday!", "error_type2")
    verify=False

  if len(session['email']) < 1:
    flash("Email", "error_type1")
    verify=False
  elif not EMAIL_REGEX.match(session['email']):
    flash("Invalid Email Format!", "error_type2")
    verify=False

  if len(request.form['password'])<9:
    flash("Password must contain at least 9 characters!!", "error_type2")
    verify=False
  elif not PSW_REGEX.match(request.form['password']):
    flash("Password requires at least one capital letter and one number!", "error_type2")
    verify=False
  elif request.form['password'] != request.form['con_password']:
    flash("Passwords do not match!!", "error_type2")
    verify=False

  if verify==True:
    session['password']= request.form['password']
    flash("Thank you! Your information has been submitted!", "confirmation")

  return redirect('/')

app.run(debug=True)
