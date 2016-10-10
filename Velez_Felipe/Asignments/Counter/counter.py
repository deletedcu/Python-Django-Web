from flask import Flask, session, render_template, redirect
app = Flask(__name__)
app.secret_key = "Felipe"

@app.route('/')
def index():
	if not 'count' in session:
		session['count'] = 0
	session['count'] +=0
	return render_template('index.html', count=session['count'])
@app.route('/process', methods=['post'])
def counter():
	if not 'count' in session:
		session['count'] = 0

	session['count'] += 1
	return redirect('/')

@app.route('/reset')
def doitnow():
	session.clear()
	return redirect('/')

app.run(debug = True)