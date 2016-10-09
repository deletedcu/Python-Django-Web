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

Long Answer:
- We store the random value between 5 and 9 in result
- We add result to the value stored in session['gold'] which was zero
- The tuple evaluates to (0, 1) = (False, True) since result is always positive, it returns 'green'
- Then we output 'farm', 'gained' (since result is always positive), and result in the formatted string
- Then every time click submit button we append the result_dictionary to our session['activities'] list,
  session['activities'] contains a list of dictionaries
"""
