from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
  return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    else:
        flash("Success! Your name is {}".format(request.form['name']))

    if len(request.form['comment']) < 1:
        flash("Comment cannot be empty!")
    elif len(request.form['comment']) > 120:
        flash("Comment cannot exceed 120 characters. Thanks for being brief!")
    else:
        flash("Success! Your comment was received.")

    print "Submitted Info"
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    return redirect('/result')

@app.route('/result')
def result_user():
  return render_template('result.html')


app.run(debug=True)
