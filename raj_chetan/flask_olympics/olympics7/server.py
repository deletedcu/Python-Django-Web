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
        print buildings[request.form['building']]
    return redirect('/')

#test
if __name__ == '__main__':
  app.run(debug = True)


"""
Explain line 24!

Depending on what value is listed in the  hidden input 
who's name is 'building', the print line will print
the value associated with the passed key in the dictionary
object 'building'. That key is pulled from the session request
request.form['building']. In this case, it pulls a randomint
from 5 to 10 because 'farm' is listed as the value for the
input name 'building'. if value is changed to 'casino', 
a randint from -50 to 50 will be displayed. if 'cave', 
0,30; if house, 0 to 5.
"""