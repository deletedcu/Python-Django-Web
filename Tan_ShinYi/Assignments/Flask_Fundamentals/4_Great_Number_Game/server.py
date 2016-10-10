from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
  if not 'message' in session:
    session['message'] = "none"
    session['color']="none"
  if not 'random_num' in session:
    session['random_num'] = random.randint(0, 100)
  print session['random_num'] #for developer's purpose
  return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
   print session['random_num']
   session['guess'] = int(request.form['guess'])
   if session['guess']>session['random_num']:
      session['message']="Too high!"
      session['color']="red"
   elif session['guess']<session['random_num']:
      session['message']="Too low!"
      session['color']="red"
   else:
      session['message']= str(session['guess']) + " was the number!"
      session['color']="green"
   return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
   session.clear()
   return redirect('/')
app.run(debug=True)
