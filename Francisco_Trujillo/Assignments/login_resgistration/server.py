from flask import Flask, render_template, flash, session, request, redirect
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key ="kwenfou4n3iru498"
bcrypt=Bcrypt(app)
mysql = MySQLConnector(app, 'frienddb')

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/registration', methods = ['POST'])
def registration():
    query = "INSERT INTO friend(fname, lname, email, pwhash, created) VALUES (:fname, :lname, :email, :pwhash, NOW())"
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email'],
        'pwd': request.form['pwd'],
        'cpwd': request.form['cpwd'],
        'pwhash': ""    }
    if len(data['fname'])< 2 or len(data['lname'])<2:
        flash("First and Last name must be at least two character long")
        return redirect('/')
    
    elif data['fname'].isalpha() != True or data['lname'].isalpha()!= True:
        flash('First name and or last name cannont contain number')
        return redirect('/')
    
    elif not EMAIL_REGEX.match(data['email']):
        flash('Please enter a valid email')
        return redirect('/')
    
    elif len(data['pwd'])<8 or len(data['cpwd'])<8:
        flash('Password must be at least 8 Characters')
        return redirect('/')
    
    elif not data['pwd'] == data['cpwd']:
        flash('Password did not match')
        return redirect('/')

    data['pwhash'] = bcrypt.generate_password_hash(data['pwd'])
    print (data['pwhash'])
    mysql.query_db(query,data)
    
    flash("Information Successfully Submitted")
    return redirect('/')

@app.route('/login', methods=['POST'])

def login():
    query = "SELECT * FROM friend WHERE email = :email"
    data = {
        'email':request.form['email'],
    }
    password = request.form['pwd']
    user = mysql.query_db(query,data)
    if not EMAIL_REGEX.match(data['email']):
        flash('Please enter a valid email')
        return redirect('/')
    elif len(user)<1:
        flash("User not found, Please register")
        return redirect('/')
    elif bcrypt.check_password_hash(user[0]['pwhash'], password):
        flash('Access Granted')
        if not 'uid'in session:
            session['uid'] = user[0]['id']
        return redirect('/home')
    else:
        flash('Email or password does not match')
        return redirect('/')
    


@app.route('/home')
def home():
    query = "SELECT * FROM friend WHERE id = :id"
    data = {'id': session['uid']}
    
    value = mysql.query_db(query,data)
    
    return render_template('home.html', value=value)
    
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)