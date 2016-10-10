from flask import Flask, render_template, session, request, redirect
import random

app= Flask(__name__ )
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    if not 'golden_number' in session:
        session['golden_number'] = random.randint(1,10)
        session['unhide'] = 'hide'
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess_work():
    guess = int(request.form['guess'])

    if guess < session['golden_number']:
        session['try'] = 'too low!'
        session['wrong'] = 'red'

    elif guess > session['golden_number']:
        session['try'] = 'too high!'
        session['wrong'] = 'red'

    else:
        session['try'] = 'correct!'
        session['wrong'] = 'green'
        session['unhide'] = 'show'
        session['butt'] = 'Play Again!'



    return redirect('/')

@app.route('/reset_game', methods = ['POST'])
def reset_game():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)
