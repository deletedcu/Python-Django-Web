from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'so_secret'

@app.route('/')
def signup():
    return render_template('signup.html')
@app.route('/user_page',methods=['POST'])
def create_users():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['fav_lang'] = request.form['fav_lang']
    session['comment'] = request.form['comment']
    session['submit'] = request.form['submit']
    return redirect('/show')
@app.route('/show')
def user_info():
    return render_template('user_page.html')

app.run(debug=True)
