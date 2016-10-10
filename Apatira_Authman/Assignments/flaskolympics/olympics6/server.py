from flask import Flask, render_template, session, request, redirect
<<<<<<< HEAD
import random
from random import randint
=======
import random 
from random import randint

>>>>>>> a5fbb0e4be104f4c2c8687849049cb538113c192
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
    print buildings
    return redirect('/')


if __name__ == '__main__':
  app.run(debug = True)


"""
Will this work?
"""
"""
Won't work until random and randint are imported. But then will assign random numbers to the keys of the buildings dictionary
