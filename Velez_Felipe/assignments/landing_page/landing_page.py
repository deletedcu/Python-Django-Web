from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')

def greetings():
	return render_template('greet.html')

@app.route('/ninjas')

def ninjas():
	return render_template('ninjas.html')

@app.route('/dojos/new')

def form():
	return render_template('form.html')

app.run(debug=True)