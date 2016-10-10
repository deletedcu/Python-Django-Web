from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key ="Felipe"

@app.route('/')
def index():
	if not 'number_to_guess' in session:
		session['hidebutton'] = 'hide'
		session['number_to_guess'] = random.randrange(0,101)
		print session['number_to_guess']

	return render_template('index.html')

@app.route('/process', methods= ['POST'])
def user_number():
	#check user number vs. number_to_guess
	session['input_number'] = int(request.form['player_guess'])

	print session['input_number']
	print session['input_number'] == session['number_to_guess']
	if session['input_number'] == session['number_to_guess']:
		session['feedback'] = "winner"
		session['formatplay'] = "correct box"
		session['format'] = "hide"
		session['hidebutton'] = 'show'
		return redirect('/')
	elif session['input_number'] > session['number_to_guess']:
		session['feedback'] = "Number too high"
		session['formatplay'] = 'play box'

	else:
		session['input_number'] < session['number_to_guess']
		session['feedback'] = "Number too low"
		session['formatplay'] = 'play box'

	return redirect('/')
	#if user number == number_to_guess return (your was the number)
	#if not return # too high or too low


	#user enter a new number and clicks in Submit again
	

@app.route('/reset', methods= ['POST'])
def clear_num():
	session.clear()
	return redirect('/')

app.run(debug = True)



