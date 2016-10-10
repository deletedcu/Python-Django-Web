from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = 'alsgkdhaslgsdsdahglas'

@app.route('/')
def index():
	if not 'num' in session:
		session['num'] = random.randrange(0,101)
		print session['num']
	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def new_guess():
	if request.form['guess'] == "":
		return redirect('/')
	else:
		check = int(request.form['guess'])
	if check == session['num']:
		if 'wrong' in session:
			session.pop('wrong')
		session['right'] = "True"
	elif check < session['num']:
		session['wrong'] = "Too low!"
	else:
		session['wrong'] = "Too high!"
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')

app.run()