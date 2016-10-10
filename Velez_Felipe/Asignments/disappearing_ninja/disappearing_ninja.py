from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninjas():
	return render_template("ninja.html", filenames='tmnt.png')

@app.route('/ninja/<ninja_color>')
def ninja(ninja_color):
	imgs ={
		'blue' : "leonardo.jpg",
		'orange' : 'michelangelo.jpg',
		'purple' : 'donatello.jpg',
		'red' : 'raphael.jpg',
	}
	if ninja_color in imgs:	
		return render_template("ninja.html", filenames = imgs[ninja_color])
	return render_template("ninja.html", filenames='notapril.jpg')
app.run(debug=True)