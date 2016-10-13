from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql =  MySQLConnector(app, 'EmailValidation')
Email_RegEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
app.secret_key = 'gg'

@app.route('/')
def pageLoad():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def formPost():

    query = "INSERT INTO email (email_address, created_at, updated_at) VALUES (:email, Now(), Now())"
    if Email_RegEX.match(request.form['email']):
        data = {'email' : request.form['email']}
        mysql.query_db(query, data)
        flash("Congratulations your email was submitted {}".format(request.form['email']), 'success')
    else:
        flash("Please enter valid email format", 'error')
        return redirect('/')
    return redirect('/resultspage')

@app.route('/resultspage')
def result():
    selectemail = "SELECT * FROM email"
    emailname = mysql.query_db(selectemail)
    print emailname
    return render_template('/resultspage.html', emailn = emailname)

@app.route('/delete', methods=['POST'])
def delete():
    delete = "DELETE FROM email ORDER BY id DESC limit 1"
    mysql.query_db(delete)
    return redirect('/resultspage')



app.run(debug=True)