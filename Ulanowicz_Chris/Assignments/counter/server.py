from flask import Flask, session, render_template, redirect
app = Flask(__name__)
app.secret_key = 'lakshdglsajgoisaeh'

@app.route('/')
def index():
	if not 'count' in session:
		session['count'] = 0
	session['count'] += 1
	return render_template('index.html')

@app.route('/ninjas', methods=['POST'])
def ninjas():
	if not 'count' in session:
		return redirect('/')
	session['count'] +=1
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')
	
app.run()