from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def form_index():
	return render_template("form_index.html")


@app.route('/users', methods=['POST'])
def create_user():
	if len(request.form['name']) < 1:
    	flash("Name cannot be empty!")
    	return redirect('/') 
  	else:
    	flash("Success! Your name is {}". format(request.form['name']))
  	
  	if len(request.form['comment']) < 1:
    	flash("Don't forget your COMMENT!")
    	return redirect('/') 
	
	session['name'] = request.form['name']
	session['dojo'] = request.form['dojo']
	session['language'] = request.form['language']
	session['comment'] = request.form['comment']
	return redirect('/show')


@app.route('/show')
def show_user():
	return render_template('users.html')   

app.run(debug=True) 
