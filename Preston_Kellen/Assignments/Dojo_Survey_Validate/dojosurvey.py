from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/users', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1:
        flash("Please enter your name!")
        return redirect('/')
    else:
        flash("Success! Your name is {}".format(request.form['name']))
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    return redirect('/')

@app.route('/show')
def show_user():
    return render_template('user.html')

app.run(debug=True)
