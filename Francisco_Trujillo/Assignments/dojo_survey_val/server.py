from flask import Flask, render_template, session, redirect, request, flash

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def users():
    print('Got post info')
    if len(request.form['name']) < 1 or len(request.form['comments'])<1:
        flash("Name or comments cannot be empty")
        return redirect('/')
    elif len(request.form['comments']) > 120:
        flash("Comments cannot be greater than 120 characater")
        return redirect('/')

    session['name'] = request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comments']=request.form['comments']
    return redirect('/results')


@app.route('/results')
def results():
     return render_template('results.html')

app.run(debug=True)
