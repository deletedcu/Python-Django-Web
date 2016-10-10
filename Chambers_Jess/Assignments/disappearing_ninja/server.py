from flask import Flask
from flask import render_template, redirect, session, request

app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def nothing():
    return render_template('sorry.html')

@app.route('/ninja')
def ninja():
    x = 'tmnt'
    return render_template('ninjas.html', x=x)

@app.route('/ninja/<any>')
def ninjas_colors_any(any):
    ninja_dict = {'blue': 'leonardo', 'red': 'raphael', 'purple': 'donatello', 'orange': 'michelangelo'}

    if any in ninja_dict:
        x = ninja_dict[any]
        return render_template('ninjas.html', x=x)

    else:
        x = 'notapril'
        return render_template('ninjas.html', x=x)

app.run(debug=True)
