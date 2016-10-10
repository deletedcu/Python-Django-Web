from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activities' in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    locations = {
        'farm':random.randint(10,20),
        'cave':random.randint(5,10),
        'house':random.randint(2,5),
        'casino':random.randint(-50,50)
    }
    if request.form['location'] in locations:
        result = locations[request.form['location']]
        session['gold'] = session['gold']+result
        result_dictionary = {
                                'class': ('red','green')[result > 0],
                                'activity': "You went to the {} and {} {} gold!".format(request.form['location'], ('lost','gained')[result > 0], result)
                            }
        session['activities'].append(result_dictionary)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)
