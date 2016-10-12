from flask import Flask, render_template, request, redirect,session
import random
app = Flask(__name__)
app.secret_key = 'secret'

too_low = 'Too Low!'
too_high = 'Too High!'
correct = 'Correct!'

@app.route('/')
def main_page():
    if not 'rand' in session:
        session['rand'] = random.randrange(0,101)
    return render_template('great_number.html')
@app.route('/test',methods = ['POST'])
def guess():
    if not 'guess' in session:
        session['guess'] = int(request.form['guess'])
    if (session['guess'] > session['rand']):
        session['p'] = too_high
    elif (session['guess'] < session['rand']):
        session['p'] = too_low
    elif (session['guess'] == session['rand']):
        session.clear()
        session['p'] = correct
    return redirect('/')
app.run(debug = True)
