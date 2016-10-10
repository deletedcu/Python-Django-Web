from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key='ThisIsSecure'

@app.route('/')
def index():
    if not 'random' in session:
        session['random']=random.randint(1,100)
        session['format']='hide'

    print(session['random'])

    return render_template('index.html')

@app.route('/sub', methods = ['POST'])
def sub():
    session['number']=int(request.form['number'])
    print(str(session['number']))
    print(session['number']==session['random'])
    if (session['number']==session['random']):
        session['feedback'] = 'You Won!!!'
        session['format'] = 'correct show'
        session['formatw'] = 'show'
        session['form'] ='hide'
    elif session['number']>session['random']:
        session['feedback'] = 'Number too high'
        session['formatw'] = 'hide'
        session['format'] = 'incorrect show'
        print('high')
    else:
        print('low')            
        session['feedback'] = 'Number too low'
        session['formatw'] = 'hide'
        session['format'] = 'incorrect show'

    return redirect('/')


@app.route('/reset', methods = ['POST'])
def reset():
    session['feedback'] = " "
    session.clear()
    return redirect('/')

app.run(debug=True)
