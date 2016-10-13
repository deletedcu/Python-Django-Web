from flask import Flask, render_template, redirect, session, request, flash
app = Flask(__name__)
app.secret_key = 'sajdgldasghewojsj'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def create():
	valid = 'true'
	if len(request.form['name']) < 1:
		valid = 'false'
		flash("Name field cannot be empty")
	if len(request.form['location']) < 1:
		valid = 'false'
		flash("Must choose a location")
	if len(request.form['language']) < 1:
		valid = 'false'
		flash("Must choose a language")
	if len(request.form['comment']) > 120:
		valid = 'false'
		flash("Comment can only be up to 120 characters")
	if valid == 'false':
		return redirect('/')
	else:
		session['name'] = request.form['name']
		session['location'] = request.form['location']
		session['language'] = request.form['language']
		session['comment'] = request.form['comment']
		return redirect('/result')

@app.route('/result')
def result():
	return render_template('result.html')

app.run()