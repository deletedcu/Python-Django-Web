from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key='This'

@app.route('/')
def start():
    if not ('num') in session:
        session['num'] = random.randrange(0,101)
    print session['num']
    num = session['num']
    if ('guess') in session:
        if int(session['guess']) == int(session['num']):
            session['answer'] = 'correct'
            session['correct'] = str(session['num']) + ' was the number!'
        elif int(session['guess']) > int(session['num']):
            session['answer'] = 'Too High!'
        else:
            session['answer'] = 'Too Low!'
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def user():
    guess = int(request.form['text'])
    session['guess']=guess
    print session['guess']
    return redirect('/')
@app.route('/reset',methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)
