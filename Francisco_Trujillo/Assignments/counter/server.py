from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/')
def index():
    if 'counter' in session:
        session['counter']+=1
    else:
        session['counter']=1
    return render_template('index.html')



@app.route('/two')
def users():
    session['counter']+=1

    return redirect('/')

@app.route('/hacker')
def hacker():
    session['counter']=0

    return redirect('/')

app.run(debug=True)
