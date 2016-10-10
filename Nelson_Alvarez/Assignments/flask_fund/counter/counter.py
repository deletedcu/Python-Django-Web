from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

count = 0

@app.route('/')
def counter():
	if not 'count' in session:
		session['count'] = 0
	session['count'] += 1
	
	return render_template("counter.html", count=session['count'])

@app.route('/process_or_some_page', methods=['POST'])
def doit():
	if not 'count' in session:
		session['count'] = 0
	
	session['count'] += 1
	return redirect('/')

@app.route('/process_or_some_page_again')
def dot():
	session.clear()
	return redirect('/')

app.run(debug=True) 	