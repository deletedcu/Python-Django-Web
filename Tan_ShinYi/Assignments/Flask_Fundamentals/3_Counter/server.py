from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
  if 'counter' not in session:
      session['counter']=0
  session['counter'] +=1
  return render_template("index.html")

@app.route('/ninjas', methods=['POST'])
def ninjas():
   session['counter'] +=1
   return redirect('/')

@app.route('/hackers', methods=['POST'])
def hackers():
   session['counter']=-1
   return redirect('/')

app.run(debug=True)
