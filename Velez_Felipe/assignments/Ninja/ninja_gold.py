from flask import Flask, render_template, redirect, session, request
import random, datetime

app = Flask(__name__)
app.secret_key = "Felipe"
@app.route('/')
def index():
	if not 'gold' in session:
		session['gold'] = 0
	if not 'activities' in session:
		session['activities'] = []
	return render_template('index.html', goldcount = session['gold'])


@app.route('/process_money', methods=['POST'])
def process():
	places = {
		'farm':random.randint(5,10),
		'cave':random.randint(5,10),
		'house':random.randint(2,5),
		'casino':random.randint(-50,50)
	}
	if request.form['place'] in places:
		result = places[request.form['place']]
		session['gold']=session['gold']+ result
		myStr = "{} {} golds from the {} ({})".format(('lost','Earned')[result > 0], abs(result), request.form['place'], datetime.datetime.now()) 
		session['activities'].append(myStr)
		return redirect('/')

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')


app.run(debug = True)