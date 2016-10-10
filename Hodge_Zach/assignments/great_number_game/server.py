from flask import Flask, session, render_template, redirect, request
import random
app = Flask(__name__)
app.secret_key = "Thisismysecretkey"

@app.route('/')
def index():
    if not 'randnum' in session:
        session['randnum'] = random.randrange(1, 101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if guess > session['randnum']:
        print guess
        return render_template('too_high.html')
    elif guess < session['randnum']:
        return render_template('too_low.html')
    else:
        return render_template('win.html', randnum=session['randnum'])

@app.route('/goback', methods=['POST'])
def goback():
    session.clear();
    return redirect('/')

app.run(debug=True)
