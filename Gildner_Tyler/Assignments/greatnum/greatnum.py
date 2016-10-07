from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def great_num():
    if not 'golden_number' in session:
        session['golden_number'] = random.randint(1,10)
        session['unhide'] = 'hide'
    return render_template('greatnum.html')

@app.route('/guess', methods=['POST'])
def random_number():
    guess = int(request.form['guess'])

    if guess < session['golden_number']:
        session['try'] = 'too low'
        session['wrong'] = 'red'

    elif guess > session['golden_number']:
        session['try'] = 'too high'
        session['wrong'] = 'red'
    else:
        session['try'] = 'Correct!'
        session['wrong'] = 'green'
        session['unhide'] = 'show'
        session['butt'] = 'Play Again!'
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_game():
    session.clear()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug = True)
