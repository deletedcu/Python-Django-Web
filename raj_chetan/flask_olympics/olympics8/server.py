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
                                'activity': "You went to the {} and {} {} gold! You now have {} gold".format(request.form['building'], ('lost','gained')[result > 0], result, session['gold'])
                            }
        session['activities'].append(result_dictionary)
    return redirect('/')


if __name__ == '__main__':
  app.run(debug = True)


"""
Explain line 24 - 31.  Will it work?  How, where what? why!?
There is a counter for result (your number of gold). The script is a 
game that, depending on which button you press, takes you to that'building'
where the rand int function comes up with a random number for the defined building
That number is added to your result as displayed as an amount of 'gold' in 
your textual result. Buttons for the other 3 buildings were missing, 
as well as a textual result for your total accumulated gold. 
We added form functionality for the other 3 building types
and added a textual display that indicates your total amount of
gold. 
"""
