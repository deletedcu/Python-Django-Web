from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/survey', methods=['POST'])
def process_survey():
	print('received post info')

	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['fav_track'] = request.form['fav_track']
	session['comment'] = request.form['comment']

	return redirect('/result')

@app.route('/result')
def display_survey_result():
	return render_template('results.html')

app.run(debug=True)