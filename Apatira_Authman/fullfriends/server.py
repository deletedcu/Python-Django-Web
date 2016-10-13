from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'friends')
print mysql

@app.route('/')
def index():
    selectAll = "SELECT * FROM friends"
    friends = mysql.query_db(selectAll)
    return render_template('index.html', friendsList = friends)

@app.route('/process', methods=['POST'])
def newFriend():
    insertFriend = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:firstName, :lastName, :occupation, Now(), Now())"
    if len(request.form['first_name'] ) < 1:
		flash("Enter Valid Name:")
		redirect('/')
	if len(request.form['last_name']) < 1:
		flash("Enter Valid Name:")
		redirect('/')
	dataCheck = {
			'firstName' : request.form['first_name'],
            'lastName' : request.form['last_name'],
            'occupation' : request.form['occupation']
            }
    friendId = mysql.query_db(insertFriend,dataCheck)
    print friendId
    return redirect('/')

@app.route('/friends/<id>', methods=['POST'])
def updateFriend(id):
	print request.form
	updateFriend = "UPDATE friends SET first_name = :newName, last_name = :lastName, occupation = :occupation WHERE id = :id"
	dataCheck = {'newName' : request.form['first_name'],
				 'lastName' : request.form['last_name'],
				 'occupation' : request.form['occupation'],
				 'id' : id
	}
	flag = mysql.query_db(updateFriend, dataCheck)
	return redirect('/')

@app.route('/friends/<id>/edit')
def editFriend(id):
	editFriend = "SELECT * FROM friends WHERE friends.id = :id"
	dataCheck = {'id' : id}
	friend = mysql.query_db(editFriend,dataCheck)
	print friend
	return render_template('/edit.html', f = friend[0])


@app.route('/delete/<id>', methods=['POST'])
def deleteFriend(id):
	print id
	deleteFriend = "DELETE FROM friends WHERE id = :id"
	dataCheck = { 'id' : id }
	delete = mysql.query_db(deleteFriend,dataCheck)
	return redirect('/')
app.run(debug=True)