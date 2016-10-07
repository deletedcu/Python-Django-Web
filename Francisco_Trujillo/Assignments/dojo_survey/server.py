from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])


def users():
    print('Got post info')
    session['name'] = request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comments']=request.form['comments']

    return redirect('/results')

@app.route('/results')
def results():
     return render_template('results.html')

app.run(debug=True)
