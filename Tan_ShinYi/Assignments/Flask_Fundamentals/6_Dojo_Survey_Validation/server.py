from flask import Flask, render_template, request, redirect, session
from flask import flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
  if not 'name' in session:
     session['name']=""
  if not 'comment' in session:
     session['comment']=""
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
   #The point of assigning these up here is so that
   #when we redirect users back to the form page,
   #they don't have to retype their comment or name
   #if that field is already filled.
   session['name'] = request.form['name']
   session['location'] = request.form['location']
   session['language'] = request.form['language']
   session['comment'] = request.form['comment']
   if len(session['name'])<1:
     flash("Name cannot be empty!")
     return redirect('/')
   elif len(session['comment'])<1:
     flash("Comment can't be empty!")
     return redirect('/')
   elif len(session['comment'])>120:
     flash("Comment can't be longer than 120 characters!")
     return redirect('/')
   else:
     print "Got Post Info"
     return redirect('/result')

@app.route('/result')
def result():
  return render_template('result.html')
app.run(debug=True)
