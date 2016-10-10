from flask import Flask, render_template, session, request, redirect
import random
from time import localtime, strftime
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activities' in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def process():
    location = {
        'farm':random.randint(10,20),
        'cave':random.randint(5,10),
        'house':random.randint(2,5),
        'casino':random.randint(-50,50),
    }
    if request.form['location'] in location:
        result = location[request.form['location']]
        session['gold'] = session['gold']+result
        result_dictionary = {
                                'activity': ("Entered a casino and lost {} gold(s)... Ouch..".format(result),
                                "Earned {} gold(s) from the {}!".format(result, request.form['location']))[result>0],
                                'time': strftime("%Y/%m/%d %I:%M %p", localtime())
                            }
        session['activities'].insert(0,str(result_dictionary['activity'])+ " ( " + str(result_dictionary['time']) + " ) ")
    return redirect('/')

@app.route('/reset') #I've included this route for dev's to reset the page
def reset():         #for the purposes of debugging
    session.clear()
    return redirect('/')

if __name__ == '__main__':
  app.run(debug = True)
