from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = 'DFG#$%^$%^JDFGWRGDJ#$%^'

def setState(result_container_state, result_text, reset_container_state, form_container_state):
	session['result_container_class'] = result_container_state
	session['result_text'] = result_text
	session['reset_button_class'] = reset_container_state
	session['form_container_class'] = form_container_state

@app.route('/')
def index():
	if not 'active_game' in session:
		session['active_game'] = True;
		session['answer'] = random.randint(1, 100)
		print('starting new game...answer {}'.format(session['answer']))

		# set up initial state
		setState('hide', '', 'hide', 'show')
	else:
		print('continuing game...answer {}'.format(session['answer']))

	return render_template('index.html')

@app.route('/process_guess', methods=['POST'])
def process_guess():
	session['guess'] = int(request.form['guess'])

	if (session['guess'] == session['answer']): 
		# game over
		setState('correct show', '{} was the number!'.format(session['answer']), 'show', 'hide')
	elif (session['guess'] < session['answer']):
		# too low
		setState('incorrect show', 'Too low!', 'hide', 'show')
	else:
		# too high
		setState('incorrect show', 'Too high!', 'hide', 'show')

	return redirect('/')

@app.route('/reset')
def reset():
	session.clear()

	return redirect('/')

# only here for debugging, since reset view controls are not always visible
@app.route('/clear')
def clear():
	session.clear()

	return redirect('/')

app.run(debug=True)