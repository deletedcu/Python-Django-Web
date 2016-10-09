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
                                'activity': "You went to the {} and {} {} gold!".format(request.form['building'], ('lost','gained')[result > 0], result)
                            }
        session['activities'].append(result_dictionary)
    return redirect('/')


if __name__ == '__main__':
  app.run(debug = True)


"""
Explain line 24 - 31.  Will it work?  How, where what? why!?
It stores the random value between 5 and 10 in result.
Then result is added to session ['gold'] and stored in session['gold']
The tuple evaluates to (0,1) = (false, true). Since result is always positive, then it returns value of 'green'.
Then it outputs 'farm' and since result is positive, it also outpurs 'gained' and the result.
last, every time the farm (submit) button is click, it appends the result_dictionary to session['activities'] list.

''
"""
