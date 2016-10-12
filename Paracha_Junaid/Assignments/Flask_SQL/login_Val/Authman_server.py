from flask import Flask, render_template, flash, session, redirect, request, Bcrypt

from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = ":):(:D!"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'mydb')


@app.route('/')
def index():
	if 'user' in session:
		return redirect('/success')
	return render_template('index.htm')


@app.route('/process', methods=['POST'])
def process():
	if not 'action' in request.form:
		flash('we got a problem...')
		return redirect('/')

	if request.form['action'] == 'login':
		query = "SELECT * FROM user WHERE email=:email;"
		data = {
			'email' : request.form['email'],
		}
		users = db.query_db(query, data)
		if len(users) == 0:
			flash("Bad email/pass combination")
			return redirect('/')

		user = users[0]
		if not bcrypt.check_password_hash(user['pwd'], request.form['pwd']):
			flash("Bad email/pass combination")
			return redirect('/')

		session['user'] = user


	elif request.form['action'] == 'register':
		# Validate user information
		# <your codez here>

		pwd = bcrypt.generate_password_hash(request.form['pwd'])

		query = "INSERT INTO user (email, pwd) VALUES (:email, :pwd);"
		data = {
			'email': request.form['email'],
			'pwd': pwd
		}
		try:
			user_id = db.query_db(query, data)
		except Exception as e:
			print e
			flash("Hey, there was a problem creating that account")
			return redirect('/')

		query = "SELECT * FROM user WHERE id = :id;"
		users = db.query_db(query, {'id' : user_id})
		session['user'] = users[0]

	return redirect('/success/')


@app.route('/success')
def success():
	if not 'user' in session:
		flash('nasty message')
		redirect('/')

	return render_template('success.htm', user=session['user'])

@app.route('/logout', methods=['POST', 'GET'])
def logout():
	#session.clear(); # if you'd like :-|
	session.pop('user');
	return redirect('/')


	mysql.query_db("SELECT * FROM post ORDER BY post.created_at DESC;")

app.run(debug=True)