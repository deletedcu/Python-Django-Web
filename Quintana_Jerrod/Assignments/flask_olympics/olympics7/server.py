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


if __name__ == '__main__':
  app.run(debug = True)


"""
Explain line 24!
 	basically, when we hit submit and it gets posted, the information that is posted is the request.form. So if ‘building’ is in the dictionary buildings, which its value - ‘farm’ is, then it prints. And when it prints, it basically uses the dictionary buildings to activate, and since it uses [request.form[‘building’]], it refers back to what was submitted/posted, which had the value of farm. so in the dictionary, farm gets a random number between 5 and 10 which is printed to the terminal.

"""
