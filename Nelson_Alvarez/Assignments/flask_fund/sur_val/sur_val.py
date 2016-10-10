from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'Thisissecret'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1:
        flash('Name field cannot be empty!')
        return redirect('/')
    else:
        flash('Success! You have a name and it is {}!!'.format(request.form['name']))
    if len(request.form['comment']) < 1:
        flash('Write a comment newt!')
        return redirect('/')
    if len(request.form['comment']) > 120:
        flash("I don't want your life story, thanks.")
        return redirect('/')

    session['name'] = request.form['name']
    session['comment'] = request.form['comment']
    session['favorite_language'] = request.form['favorite_language']
    session['dojo_select'] = request.form['dojo_select']
    return redirect('/show')

@app.route('/show')
def show_user():
  return render_template('user.html')

app.run(debug=True)