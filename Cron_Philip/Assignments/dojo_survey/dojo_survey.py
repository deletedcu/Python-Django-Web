from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def index():
  return render_template("index.html")
@app.route('/', methods=['POST'])
def form_page():
    print "Got Post Info"
    print request.form
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result_page():
    return render_template('result.html')

app.run(debug=True)
