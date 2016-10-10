from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key= 'This'

@app.route('/')
def counter():
    if not ('counter') in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('counter.html', counter = session['counter'])
@app.route('/ninja')
def ninja():
    session['counter'] += 1
    return redirect('/')
@app.route('/hacker')
def hacker():
    session['counter'] = -1
    return redirect('/')
app.run(debug=True)
