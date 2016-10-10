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
let’s take it from the top
	so first, it checks if the post info that was submitted had a value in the dictionary, which its value, farm, is. Then, it creates a variable, result, which activates the farm key in buildings, since that’s all ‘request.form[‘building’]’ is, the key farm in the dictionary buildings. so it activates the farm key, which makes result equal a number between 5 and 10. Then it makes the session[‘gold’] which is currently zero, equal itself plus the random number. then it creates a new dictionary and has two keys. the first key, class, has the value of red and green, and the [] is referring to the index, which if result is greater than 0, which it always is, it is true and equals one so green is always selected. So then activity is a string which has farm as the first bracket, lost or gained [] thing is the second bracket, which acts as the same as red and green so gained is always selected. and the result or random number is the final bracket. It then adds the entire new dictionary to the session activities, to be printed upon the submit button.
"""
