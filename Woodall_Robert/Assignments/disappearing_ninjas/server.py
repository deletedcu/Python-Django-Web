from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def display_ninjas():
	return render_template('ninja.html', filename='tmnt.png')

@app.route('/ninja/<color>')
def display_ninja(color):
	imgs = {
		'blue': 'leonardo.jpg',
		'orange': 'michelangelo.jpg',
		'red': 'raphael.jpg',
		'purple': 'donatello.jpg'
	}

	if color in imgs:
		return render_template('ninja.html', filename=imgs[color])
	
	return render_template('ninja.html', filename='notapril.jpg')

app.run(debug=True)