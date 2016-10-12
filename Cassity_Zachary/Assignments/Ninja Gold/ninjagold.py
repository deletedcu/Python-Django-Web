from flask import Flask, render_template, request, redirect,session
import random
app = Flask(__name__)
app.secret_key = 'secret'
@app.route('/')
def main_page():
    if not 'gold' in session:
        session['gold'] = 0
    return render_template('main_page.html')

@app.route('/process_money', methods = ['POST'])
def process():
    if (request.form['building'] == 'farm'):
        session['gold'] += random.randrange(10,20)
        return redirect('/')
    elif(request.form['building'] == 'cave'):
        session['gold'] += random.randrange(5,20)
        return redirect('/')
    elif(request.form['building'] == 'house'):
        session['gold'] += random.randrange(5,20)
        return redirect('/')
    elif(request.form['building'] == 'casino'):
        session['gold'] += random.randrange(-50,50)
        if(session['gold'] < 0):
            session['gold'] = 0
        return redirect('/')
@app.route('/reset',methods =['POST'])
def reset():
    if(request.form['reset'] == 'reset'):
        session.clear()
        return redirect('/')

app.run(debug = True)
