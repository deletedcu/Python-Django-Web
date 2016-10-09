from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process/<id>', methods = ['POST'])
def process(id):
    print ("I love flask! And {}".format(id))
    return redirect('/')


if __name__ == '__main__':
  app.run(debug = True)


"""
Will this work?  What
What will this print???
no it will not work if you wanted it to show on the page, when it prints, it prints in the terminal. In order to print onto the page we would have to render the template index.html and use sessions, or other such methods. If the terminal was your goal then it does work, it prints I love flask! and peaches
"""
