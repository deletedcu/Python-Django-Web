from flask import Flask, render_template  
app = Flask(__name__)                     
@app.route('/')
def index2():
	return render_template("index2.html")

@app.route('/ninjas')
def ninja():
	return render_template("ninjas.html")

@app.route('/dojos/new')
def dojo():
	return render_template("dojos.html")

app.run(debug=True) 