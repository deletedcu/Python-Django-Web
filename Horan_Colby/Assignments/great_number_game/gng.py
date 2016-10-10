from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
import random

app = Flask(__name__)
app.secret_key = 'SEEEEEEEECRET'

@app.route('/')
def index():
	if not 'bingo' in session:
		session['bingo'] = random.randint(0,100)
		session['hidetoggle'] = 'hide'
	return render_template('gng.html')
 

@app.route('/guess', methods=['post'])
def guess():

	guess = int(request.form['guess'])

	if guess < session['bingo']:
		session['try'] = 'Too Fucking Low!'
		session['class'] = 'red'
	elif guess > session['bingo']:
		session['try'] = "Too Fucking High!"
		session['class'] = 'red'
	else:
		session['try'] = 'YOU FUCKING GOT IT!'
		session['class'] = 'green'
		session['hidetoggle'] = 'show'

	return redirect('/')


@app.route('/reset', methods= ['post'])
def reset():
	session.clear()
	return redirect('/')


app.run(debug=True)
