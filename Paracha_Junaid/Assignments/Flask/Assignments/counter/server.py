from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    if not 'count' in session:
      session['count'] = 0
    session['count'] += 1

    return render_template('index.html', count=session['count'])

@app.route('/plus2', methods = ['POST'])
def process():
    if not 'count' in session:
      session['count'] = 0
    session['count'] += 1
     
    return redirect('/')

@app.route('/reset')
def reset():
  session['count'] = 0
  
  return redirect('/')

if __name__ == '__main__':
  app.run(debug = True)
