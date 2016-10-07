from flask import Flask, session, render_template, redirect, request
import random

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activities' in session:
        session['activities'] = []

    return render_template('index.html', gold=session['gold'])

@app.route('/process_money', methods=['POST'])
def process():
    locations = {
        'farm': random.randint(10, 21),
        'cave': random.randint(5, 11),
        'house': random.randint(2, 6),
        'casino': random.randint(-50,51)
    }

    if request.form['locations'] in locations:
        result = locations[request.form['locations']]
        session['gold'] = session['gold'] + result
        result_dictionary = {
                                'class': ('red','green')[result > 0],
                                'activity': "You went to the {} and {} {} gold! You now have {} gold!".format(request.form['locations'],
                                ('lost','gained')[result > 0], result, session['gold'])
                            }
    session['activities'].append(result_dictionary)
    return redirect('/')
app.run(debug=True)
