from flask import Flask, render_template, session, request, redirect
import random
import datetime

app = Flask(__name__)
app.secret_key = 'gold_game_gg'

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activities' in session:
        session['activities'] = []
    return render_template('home.html')

# This will process the function to add gold then log the activity
@app.route('/process_money', methods = ['POST'])
def money_bags():
    jobs = {
        'farm':random.randint(10,20),
        'cave':random.randint(5,10),
        'house':random.randint(2,5),
        'casino':random.randint(-50,50)
    }
    if request.form['job'] in jobs:
        income = jobs[request.form['job']]
        session['gold'] += income
        if income >= 0:
            income_string = ['gained', '!', 'green']

        elif income < 0:
            income_string = ['lost', '... Ouch...', 'red']

        timestamp = datetime.datetime.now()
        activity =  "You went to the {} and {} {} gold{} ({})".format(request.form['job'], income_string[0], income, income_string[1], timestamp)
        activity_dict = {
            'activity' : activity,
            'color' : income_string[2]
        }
        session['activities'].append(activity_dict)

    return redirect('/')


@app.route('/reset', methods = ['POST'])
def reset_game():
    session.clear()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)
