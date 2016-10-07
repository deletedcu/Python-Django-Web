from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "SecretKeyz"
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/results', methods=['POST'])
def show_results():
	print "Server has received user input."
	#return render_template("results.html")
	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['fav_lang'] = request.form['fav_lang']
	session['comment'] = request.form['comment']
	return redirect('/')

@app.route('/show')
def show_user():
	return render_template('user.html', name=session['name'], location=session['location'], fav_lang=session['fav_lang'], comment=session['comment'])
app.run(debug=True)