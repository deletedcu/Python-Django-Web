
from flask import Flask, render_template, session, request, redirect, flash
import re
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[A-Z])\w{8,}$')
app = Flask(__name__)
app.secret_key = 'my_secret_key'
mysql = MySQLConnector(app, 'friends')

@app.route('/')
def index():
    login_user = mysql.query_db("SELECT first_name, last_name, email, users.id, DATE_FORMAT(users.created_at,'%d/%m/%Y %h:%i %p') as created_at FROM users")
    
    return render_template('index.html', login_user = login_user)

@app.route('/show', methods = ['POST'])
def friends_index():
    session['login_id'] = request.form['login_user']   
    session['users_info'] = mysql.query_db("SELECT u2.id as id, u2.email as User_Name, u2.first_name as First_Name, u2.last_name as Last_Name, DATE_FORMAT(users.created_at,'%d/%m/%Y %h:%i %p') as created_at FROM friends.users LEFT JOIN friendship as f ON f.user_id=users.id LEFT JOIN users as u2 ON u2.id =f.Friend_id WHERE f.User_id='"+session['login_id'] +"'")

    return redirect('/')  

@app.route('/friend', methods = ['POST'])
def add_friend():    
    if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1:
        flash("Fields cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif not request.form['first_name'].isalpha():
        flash("Invalid Name! First Name cannot contain and characters or numbers")
    elif not request.form['last_name'].isalpha():
        flash("Invalid Name! Last Name cannot contain and characters or numbers")
    else:
        flash("Success!")
        Str = "INSERT INTO users(first_name, last_name, email, created_at, updated_at) VALUE (:first_name, :last_name, :user_email, NOW(), NOW())"
        data = { 'first_name':request.form['first_name'],'last_name':request.form['last_name'],'user_email':request.form['email']}
        
        friend_id_num = mysql.query_db(Str,data)
        print friend_id_num
        print session['login_id']
        Str = "INSERT INTO friendship(user_id, friend_id, created_at, updated_at) VALUE (:user_id, :friend_id, NOW(), NOW())"
        data = { 'user_id':session['login_id'] ,'friend_id':friend_id_num}
        mysql.query_db(Str,data)
    return redirect('/')

@app.route('/<id>/edit')
def success(id):
    users_info_edit = mysql.query_db("SELECT users.id as id, users.email as User_Name, users.first_name as First_Name, users.last_name as Last_Name, DATE_FORMAT(users.created_at,'%d/%m/%Y %h:%i %p') as created_at FROM friends.users WHERE users.id='"+id+"'")
    print users_info_edit
    return render_template('edit.html', users_edit = users_info_edit)

@app.route('/friend/<id>', methods = ['POST'])
def update(id):
    Str = "UPDATE friends.users SET email = :email, first_name = :first_name, last_name = :last_name WHERE id = :id"
    data = {
             'email': request.form['email'], 
             'first_name': request.form['first_name'], 
             'last_name':  request.form['last_name'],
             'id': id
           }
       
    print mysql.query_db(Str,data)
        
    return redirect('/'+id+'/edit')
@app.route('/friend/<id>/delete', methods = ['POST'])
def delete(id):
    Str = "DELETE FROM friends.users WHERE id= :id"
    data = { 'id':id }
       
    print mysql.query_db(Str,data)
        
    return redirect('/')

if __name__ == '__main__':
  app.run(debug = True)
  
# @app.route('/register', methods = ['POST'])
# def register():
#     valid = True
#     if len(request.form['email']) < 1 :
#         flash("Fields cannot be blank!")
#         valid = False
#         return redirect('/')
#     elif not EMAIL_REGEX.match(request.form['email']):
#         flash("Invalid Email Address!")   
#         valid = False
#         return redirect('/')
#     if valid == True:
#         Str = "INSERT INTO user(email, created_at, updated_at) VALUE (:user_email, NOW(), NOW())"
#         data = { 'user_email': request.form['email'] }
#         print data
#         print mysql.query_db(Str,data)
#         session['added_email'] = request.form['email']
#         return redirect('/success')