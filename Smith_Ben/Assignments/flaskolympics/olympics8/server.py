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
                                'activity': "You went to the {} and {} {} gold! You now have {} gold.".format(request.form['building'], ('lost','gained')[result > 0], result, session['gold'])
                            }
        session['activities'].append(result_dictionary)
    return redirect('/')


if __name__ == '__main__':
  app.run(debug = True)


"""
Explain line 24 - 31.  Will it work?  How, where what? why!?
I fixed it.
The user has an option of inputs to choose from.  The inputs
are from the dictionary 'building' by selecting one of the keys
it will give an interger value that is referenced from the key.
results = the 'building' dictionary as well and assigns
a class and activity.
"""
