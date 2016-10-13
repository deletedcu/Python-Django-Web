from flask import Flask, render_template, request, redirect, session, flash
import datetime
import re
import random

app = Flask(__name__)
app.secret_key = 'rocksteady'

Email_REGEX = re.compile(r'[^\s*$][1,120]')

@app.route('/')
def index():
	return render_template('FormValidation.html')

@app.route('/process', methods=['POST'])
def process():
	if not 'name' in session:
		session['name'] = ''
	if not 'comment' in session:
		session['comment'] = ''
	if not 'location' in session:
		session['location'] = ''
	if not 'fav' in session:
		session['fav'] = ''
	session['location'] = request.form['locations']
	session['fav'] = request.form['favorites']
	session['comment'] = request.form['commentArea']
	session['name'] = request.form['full_name']
	if  Email_REGEX.match(request.form['full_name']):
		print len(request.form['full_name'])
		flash("Your name cannot be empty!")	
		return redirect('/')
	else:
		print len(request.form['full_name'])
		flash("Success! Your name is {}".format(request.form['full_name']))
	return redirect('/FormResults.html')

@app.route('/FormResults.html')
def pageLoad():
	return render_template('/FormResults.html')	
app.run(debug=True)