from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'felipe'
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/info', methods=['POST'])
def create_user():
	session['name'] = request.form['name']
	session['dojo'] = request.form['dojo']
	session['language'] = request.form['language']
	session['comment'] = request.form['comment']
	# session['submit'] = request.form['submit']
	return redirect('/results')

@app.route('/results')
def results():
	return render_template("results.html")
app.run(debug=True)