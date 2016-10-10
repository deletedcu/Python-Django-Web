
from flask import Flask 
from flask import render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '123'

@app.route('/')

def hello_world():
	return render_template('index.html', name='Junaid')


@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   session['name'] = request.form['name']
   session['location'] = request.form['location']
   session['language'] = request.form['language']
   session['comment'] = request.form['comment']
   # redirects back to the '/' route
   return redirect('/')

@app.route('/show')
def show_user():
  return render_template('user.html')

app.run(debug=True)
