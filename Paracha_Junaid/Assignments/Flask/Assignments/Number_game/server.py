from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    if not 'random_num' in session:
      session['random_num'] = random.randint(1,100)
    if not 'x' in session:
       session['x'] = {}
    
    print session['random_num']
    print session['x'] 
    return render_template('index.html')

@app.route('/again')
def again():
    print session['random_num']
    print session['x'] 
    session.pop('random_num', 'x') 
    return redirect('/')

@app.route('/guess', methods = ['POST'])
def process():
    user_guess = int(request.form['user_guess'])
    ans = { 'content':str(session['random_num'])+" was the number", 'class':'green','type':'submit'}
    low = { 'content':"too low", 'class':'red','type':'hidden'}
    high = { 'content':"too high",'class':'red','type':'hidden'}  
    # session['x'] = {}
    if user_guess == session['random_num']:
     session['x'] = ans
    elif user_guess < session['random_num']:
      session['x'] = low
    else: session['x'] = high
    
    print session['x'] 
    print type(session['x'])
    return render_template('index.html')


 

if __name__ == '__main__':
  app.run(debug = True)
