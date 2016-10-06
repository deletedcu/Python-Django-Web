from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def landing_page():
	return render_template('index.html')
@app.route('/ninjas')
def ninjas():
	return render_template('ninjas.html')
@app.route('/dojos/new')
def dojos():
	return render_template('dojos.html')
app.run(debug=True)