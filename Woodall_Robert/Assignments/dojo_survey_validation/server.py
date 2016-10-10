from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/survey', methods=['POST'])
def process_survey():
	print('received post info')

	if (len(request.form['name']) < 1) or (len(request.form['comment']) < 1):
		flash('Name and comment fields cannot be empty!')
		return redirect('/')
	elif len(request.form['comment']) > 120:
		flash('Comment field has a max of 120 characters!')
		return redirect('/')

	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['fav_track'] = request.form['fav_track']
	session['comment'] = request.form['comment']

	return redirect('/result')

@app.route('/result')
def display_survey_result():
	return render_template('results.html')

app.run(debug=True)

