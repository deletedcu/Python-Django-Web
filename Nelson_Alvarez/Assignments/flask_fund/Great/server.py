from flask import Flask, render_template, request, redirect, session
import random 

app = Flask(__name__)
app.secret_key = "ThisIsSecret"


@app.route('/')
def index():
	if not 'golden_num' in session:
		session['golden_num'] = random.randint(1,100)
		session['hide']= 'hide'
	return render_template("index.html")
 
@app.route('/guess', methods=['POST'])
def guess_work():
	guess = int(request.form['guess'])

	if guess < session['golden_num']:
		session['try'] = 'too low'
		session['wrong'] ='red'

	elif guess > session['golden_num']:
		session['try'] = 'too high'
		session['wrong'] = 'red'

	else:
		session['try'] = 'Correct!' 
		session['wrong'] = 'green'
		session['hide'] = ''
		session['butt'] = 'Play again!'

	return redirect('/')


@app.route('/reset_game', methods=['POST'])
def reset_game():
	session.clear()
	return redirect('/')


app.run(debug=True) 