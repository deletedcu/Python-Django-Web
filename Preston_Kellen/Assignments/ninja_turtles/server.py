from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'secretninjas'

ninja_dict = {
    'blue' : 'leonardo',
    'orange' : 'michelangelo',
    'red' : 'raphael',
    'purple' : 'donatello',
    'ninja' : 'tmnt',
    '' : 'notapril'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    x = ninja_dict['ninja']
    return render_template('color.html', x=x)

@app.route('/ninja/<color>')
def ninja(color):
    if color in ninja_dict:
        x = ninja_dict[color]
        return render_template('color.html', x=x)
    else:
        x = 'notapril'
        return render_template('color.html', x=x)


if __name__ == '__main__':
    app.run(debug = True)
