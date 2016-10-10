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

Line 24: is another way of saying 'this code looks whack'
Line 25 - 31: Checks if the post info that was submitted had a value in the dictionary. The value farm exists. Then, it creates a variable called 'result', which activates the farm key in buildings. Farm key makes var 'result', equal a number between 5 and 10. Then it makes the session[‘gold’] which is currently 0, equal to itself plus the random number. A new dictionary with two keys is created. The first key, 'class', has the value of 'red' and 'green'. Green is selected by the index value, random integer result compared to 0. In the above code sampling, it is always true and equals 1.  Green is the the index value of 1. Green is always set. In the same way, 'gained' is always set. It then appends the string of text to the 'activities' session. and updates the page. 

    And, the html,
"""
