
from flask import Flask, render_template, session, request, redirect, flash
import re
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[A-Z])\w{8,}$')
app = Flask(__name__)
app.secret_key = 'my_secret_key'
mysql = MySQLConnector(app, 'email_validation')

@app.route('/')
def index():
    
    return render_template('index.html')
@app.route('/register', methods = ['POST'])
def register():
    valid = True
    if len(request.form['email']) < 1 :
        flash("Fields cannot be blank!")
        valid = False
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")   
        valid = False
        return redirect('/')
    if valid == True:
        Str = "INSERT INTO user(email, created_at, updated_at) VALUE (:user_email, NOW(), NOW())"
        data = { 'user_email': request.form['email'] }
        print data
        print mysql.query_db(Str,data)
        session['added_email'] = request.form['email']
        return redirect('/success')

@app.route('/success')
def success():
    users_info = mysql.query_db("SELECT user.email, user.id, DATE_FORMAT(user.created_at,'%d/%m/%Y %h:%i %p') as created_at FROM email_validation.user")
    print users_info
    return render_template('user.html', users = users_info)

@app.route('/delete/<id>')
def delete(id):
    Str = "DELETE FROM email_validation.user WHERE id= :id"
    data = { 'id':id }
       
    print mysql.query_db(Str,data)
        
    return redirect('/success')

if __name__ == '__main__':
  app.run(debug = True)
  
