from flask import Flask, session, redirect, render_template, request
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key='This'

@app.route('/')
def start():
    if not ('gold') in session:
        session['gold'] = 0;
    if not ('activities') in session:
        session['activities'] = {}
    return render_template('index.html', gold = session['gold'], activities = session['activities'])

@app.route('/process_money', methods=['POST'])
def money():
    now = datetime.now()
    buildings = {
        'farm': random.randrange(10,21),
        'cave': random.randrange(5,11),
        'house': random.randrange(2,6),
        'casino': random.randrange(0,51)
    }
    session['green'] = 'green'
    session['red']='red'
    if request.form['building'] == 'casino':
        result = buildings[request.form['building']]
        rand = random.randrange(0,2)
        if rand == 0:
            session['gold'] += result
            session['activities'].update({'Entered a casion and gained {} gold! ({})'.format(buildings[request.form['building']], now): session['green']})
        else:
            session['gold'] -= result
            session['activities'].update({'Entered a casion and lost {} gold...Ouch... ({})'.format(buildings[request.form['building']], now): session['red']})
    elif request.form['building'] in buildings:
        result = buildings[request.form['building']]
        session['gold'] += result
        session['activities'].update({'Earned {} gold from the farm! ({})'.format(buildings[request.form['building']], now): session['green']})
    return redirect('/')

app.run(debug=True)
