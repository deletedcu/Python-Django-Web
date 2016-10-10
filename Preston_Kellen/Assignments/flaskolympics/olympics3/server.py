from flask import Flask, render_template,session
app = Flask(__name__)
app.secret_key= "ThisIsSecret"

@app.route('/')
def myfirstfunction():
    if not 'title' in session:
        session['title'] = 'hello world'
    return render_template('index.html', name="Mike")

if __name__ == '__main__':
  app.run(debug = True)
