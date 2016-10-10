from flask import Flask, render_template, redirect, session, request
import random, datetime

app = Flask(__name__)
app.secret_key='98t5unggno56'

@app.route('/')
def index():
    if not'gold' in session:
        session['gold'] = 0
        session['click']= 0

        session['message']=[]
    return render_template('index.html')


@app.route('/process_money', methods = ['POST'])
def money():
    earn= ""


    session['click']=request.form['action']
    print(session['click'])

    if session['click']=='farm':
        earn = random.randint(10,20)
        session['gold']+=earn
        session['message'].append(" Ninja has earned {} from {}!: ({})".format(earn,session['click'], datetime.datetime.now()))


    elif session['click']=='cave':
        earn=random.randint(5,10)
        session['gold']+=earn
        session['message'].append(" Ninja has earned {} from {}!: ({})".format(earn,session['click'], datetime.datetime.now()))

    elif session['click']=='house':
        earn=random.randint(2,5)
        session['gold']+=earn
        session['message'].append(" Ninja has earned {} from {}!: ({})".format(earn,session['click'], datetime.datetime.now()))


    else:
        earn=random.randint(-50,50)
        session['gold']=earn
        if earn < 0:
            session['message'].append(" Ninja has lost {} from {}!: ({})".format(earn,session['click'], datetime.datetime.now()))

        else:
            session['message'].append(" Ninja has earned {} from {}!: ({})".format(earn,session['click'], datetime.datetime.now()))


    return redirect('/')


@app.route('/reset', methods = ['POST'])
def reset():
    session['feedback'] = " "
    session.clear()
    return redirect('/')

app.run(debug=True)
