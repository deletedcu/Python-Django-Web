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
Explain line 24! --->
The value "farm" was assigned to the key "building" when the submit
button was pressed in the index view. Then on the backend, we looked
into the buildings dictionary and saw that "farm" was indeed a key
that existed and thus we printed a random value between 5-10.
"""
