from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET'])
def index():

    return render_template('testing.html')


@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("need first name")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
    elif not request.form['first_name'].isalpha():
        flash('have a name?')
    elif not request.form['last_name'].isalpha():
        flash('ill name you Bambino')
    elif request.form['password'] < 8:
        flash('Password must be less than 8 characters')
    elif request.form['password'] != request.form['cpassword']:
        flash('did not match password')

    else:
        flash('O MAN!!! YOU GOT IT!!')

    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['cpassword'] = request.form['cpassword']

    return redirect('/')
app.run(debug=True)