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

When submit is clicked, it posts to the /process function. The process function declares a dictionary of 'buildings'. If the value of request.form['building'] from the index.html is found in the dictionary, which it is, because its value is farm, then it processes the value of the key 'farm', which is declared as a random integer between 5,10 in our dictionary. A random integer is printed in the terminal.

"""
