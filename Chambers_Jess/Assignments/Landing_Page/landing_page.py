from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def landing_page():
  return render_template('index.html', name="Jess")

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', phrase="Click to See", phrase2="Noyce")

@app.route('/dojos/new')
def dojos():
    return render_template('dojos.html')

app.run(debug=True)
