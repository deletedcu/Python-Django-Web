from flask import Flask, render_template, session, redirect, request, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'authentica_everything'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validation', methods = ['POST'])
def validation():
    if not request.form['first_name'].isalpha():
        flash('Please enter your first name.')
    else:
        flash('First name saved.')

    if not request.form['last_name'].isalpha():
        flash('Please enter your last name.')
    else:
        flash('Last name saved.')

    if len(request.form['birthdate']) < 1:
        flash('Please enter a birthdate.')
    # elif not DATE_REGEX.match(request.form['birthdate']):
    #     flash('Snatch the pebble from my hand, grasshopper.')
    else:
        flash('Birthdate saved.')

    if len(request.form['email']) < 1:
        flash('Please enter your email address.')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Email does not exsist.')
    else:
        flash('Email saved.')

    if len(request.form['pword']) < 8:
        flash('Please create a password.')
    # elif not PASS_REGEX.match(request.form['pword']):
    #     flash('Password must be at least 9 characters and contain at least 1 number.')
    else:
        flash('Password Entered.')

    if request.form['pword_conf'] != request.form['pword']:
        flash('Password does not match.')
    else:
        flash('Passwords match.')

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['birthdate'] = request.form['birthdate']
    session['email'] = request.form['email']
    session['pword'] = request.form['pword']
    session['pword_conf'] = request.form['pword_conf']
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)
