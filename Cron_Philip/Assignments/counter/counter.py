from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def counter_session():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1

@app.route('/')
def keep_count():
    counter_session()
    return render_template("index.html")

@app.route('/add')
def add():
    session['counter'] = session['counter'] + 1
    return redirect(url_for('keep_count'))

@app.route('/clear')
def clear():
    session.clear()
    return redirect(url_for('keep_count'))

app.run(debug=True)
