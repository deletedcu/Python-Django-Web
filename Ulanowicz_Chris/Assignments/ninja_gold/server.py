from flask import Flask, render_template, redirect, session, request
import random
import datetime

app = Flask(__name__)
app.secret_key = "12345678asdfghjk"

@app.route('/')
def index():
	if not 'gold' in session:
		session['gold'] = 0
	if not 'log' in session:
		session['log'] = ["Thanks for joining the game!"]
	return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')

@app.route('/process_money', methods=['POST'])
def process():
	when = datetime.datetime.now()
	if request.form['arena'] == 'farm':
		money = random.randint(10,20)
		msg = "Baled some hay and earned " + str(money) + " gold (" + str(when) + ")"
		session['log'].append(msg)
		session['gold'] += money
	elif request.form['arena'] == 'cave':
		money = random.randint(5,10)
		msg = "Mined some ore and earned " + str(money) + " gold (" + str(when) + ")"
		session['log'].append(msg)
		session['gold'] += money
	elif request.form['arena'] == 'house':
		money = random.randint(2,5)
		msg = "Cleaned some dishes and earned " + str(money) + " gold (" + str(when) + ")"
		session['log'].append(msg)
		session['gold'] += money
	else:
		odds = random.randint(1,10)
		if odds < 3:
			money = random.randint(0,50)
			msg = "Got lucky and won " + str(money) + " gold (" + str(when) + ")"
			session['log'].append(msg)
			session['gold'] += money
		else:
			money = random.randint(-50,0)
			msg = "Lost " + str(abs(money)) + " gold at the casino (" + str(when) + ")"
			session['log'].append(msg)
			session['gold'] += money
	return redirect('/')

app.run()