from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activities' in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    buildings = {
        'farm':random.randint(5,10),
        'casino':random.randint(-50,50),
        'cave':random.randint(0,30),
        'house':random.randint(0,5)
    }
    if request.form['building'] in buildings:
        """ OMG What???"""
        result = buildings[request.form['building']]
        session['gold'] = session['gold']+result
        result_dictionary = {
                                'class': ('red','green')[result > 0],
                                'activity': "You went to the {} and {} {} gold! You nw have {} gold!".format(
                                request.form['building'],
                                ('lost','gained')[result > 0], result,
                                session['gold'])
                            }
        session['activities'].append(result_dictionary)
    return redirect('/')


if __name__ == '__main__':
  app.run(debug = True)


"""
Explain line 24 - 31.  Will it work?  How, where what? why!? -->
Based on the input of the user, the 'building' key is assigned a value
(which at default is farm) and then the result variable is assigned
a random number based on the range associated with the location inputted
by the user referenced from the buildings dictionary. Since the default is
farm we will always have a result of 5-8.

Session['gold'] saves the information on total gold, adding the result
from the most recent trip to the farm to your current checking account.

Result dictionary helps assign what should be printed to the user based on their
results.

Session['activities'] adds a new output message based on results.
"""
