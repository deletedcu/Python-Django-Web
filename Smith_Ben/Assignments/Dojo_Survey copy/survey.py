from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'This is Secret'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/back')
def back():
	session['back'] = request.form['back']
	return redirect('/')

@app.route('/users', methods=['POST'])
def create_user():
	if len(request.form['name']) < 1:
		flash('Name needs sumthin foo. Grow UP!')
		return redirect('/')
	else:
		flash('YAY! you finally learned something! Your name is {}'.format(request.form['name']))
	if len(request.form['comment']) < 1:
		flash('Name a comment')
		return redirect('/')
	if len(request.form['comment']) > 120:
		flash('tl;dr')
		return redirect('/')

	session['name'] = request.form['name']
	session['Location'] = request.form['Location']
	session['Language'] = request.form['Language']
	session['comment'] = request.form['comment']

	return redirect('/result')

@app.route('/result')
def result():
	return render_template("result.html")

app.run(debug=True)