from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninja')
def ninja1():
  return render_template("ninja.html", nav="none")

@app.route('/ninja/<nav>')
def ninja2(nav):
  return render_template("ninja.html", nav=nav)

app.run(debug=True)
