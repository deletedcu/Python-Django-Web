from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if not 'count' in session:
        session['count'] = 0
    session['count'] += 1

    return render_template("index.html", count=session['count'])

@app.route('/process', methods=['POST'])
def process():
    if not 'count' in session:
        session['count'] = 0

    session['count'] += 1
    return redirect("/")

@app.route('/process_clear', methods=['POST'])
def clear():
    session['count'] = -1
    session.clear()
    return redirect('/')


app.run(debug=True)
