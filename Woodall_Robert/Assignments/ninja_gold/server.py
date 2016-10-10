from flask import Flask, redirect, request, render_template, session
import random, datetime

app = Flask(__name__)
app.secret_key = '@#$%#&%**%^%^%^#%^*(*'

@app.route('/')
def index():
	if (not 'gold_count' in session) or (not 'activities' in session):
		session['gold_count'] = 0
		session['activities'] = []

	return render_template('index.html', gold_count = session['gold_count'])

def store_data(tuple_range, location):
	activity_str = ''
	count = random.randint(tuple_range[0], tuple_range[1])

	if location != 'casino':
		session['gold_count'] += count
		activity_str = 'Earned {} golds from the {}! ({})'.format(count, location, datetime.datetime.now())
	else:
		if (random.randint(0, 1) == 0):
			session['gold_count'] -= count
			activity_str = 'Lost {} golds from the {}...quit gambling! ({})'.format(count, location, datetime.datetime.now())
		else:
			session['gold_count'] += count
			activity_str = 'Earned {} golds from the {}! ({})'.format(count, location, datetime.datetime.now())

	session['activities'].append(activity_str)
		
@app.route('/process_gold', methods=['POST'])
def process_gold():
	location = request.form['location']

	if location == 'farm':
		store_data((10, 20), 'farm')
	elif location == 'cave':
		store_data((5, 10), 'cave')
	elif location == 'house':
		store_data((2, 5), 'house')
	elif location == 'casino':
		store_data((0, 50), 'casino')
		
	return redirect('/')

@app.route('/reset')
def reset():
	session.clear()

	return redirect('/')
app.run(debug=True)