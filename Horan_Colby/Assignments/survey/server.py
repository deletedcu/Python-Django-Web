from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'Thisissecret'
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
	session['name'] = request.form['name']
	session['comment'] = request.form['comment']
	session['favorite_language'] = request.form['favorite_language']
	session['dojo_select'] = request.form['dojo_select']
	if len(request.form['name']) < 1:
		flash("Name field cannot be empty")
		return redirect('/')
	if len(request.form['comment']) < 1:
		flash("You must enter a comment, or die")
		return redirect('/')
	return redirect('/show')

@app.route('/users', methods=['post'])
def process():
	return redirect('/')

@app.route('/show')
def show_user():
	return render_template('user.html')
app.run(debug=True)
