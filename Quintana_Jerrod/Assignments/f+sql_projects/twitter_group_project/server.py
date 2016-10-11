from flask import Flask, redirect, render_template
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'twitter')

@app.route('/')
def landing():
    tweet = mysql.query_db('SELECT tweet, DATE_FORMAT(tweets.created_at, "%b %d %Y %h:%i %p") AS created_at, users.handle AS user FROM tweets JOIN users ON users.id = tweets.user_id ORDER BY created_at DESC')

    # color = mysql.query_db('SELECT tweet_id, user_id FROM faves WHERE user_id = 2')

    return render_template('index.html', tweet = tweet, color=color)


app.run(debug=True)
