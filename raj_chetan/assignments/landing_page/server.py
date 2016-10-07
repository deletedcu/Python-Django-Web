#server script utilizing flask for landing page assignment

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('index.html', my_var_str = "test variable", my_var_int = 5)

@app.route('/ninjas')
def ninja_page():
	return render_template('ninja.html', ninja_var= "this is my ninja page")

@app.route('/dojos/new')
def dojos_new():
	return render_template('dojo_new.html', new_var = "this is my new page in the dojo directory")






app.run(debug=True)	 