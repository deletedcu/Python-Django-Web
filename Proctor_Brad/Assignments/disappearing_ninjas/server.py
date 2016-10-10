from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = 'q2489jfv9opfjvj89ewj'
whatever = 'tmnt'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja', methods=['POST'])
def ninja():
    return render_template('ninja.html', whatever=whatever)

@app.route('/ninja/<color>')
def show_ninja_color(color):
    ninjaDict = {'blue':'leonardo','orange':'michelangelo','red':'raphael','purple':'donatello'}

    if color in ninjaDict:
        whatever = ninjaDict[color]
    else:
        whatever = 'notapril'
    return render_template('ninja.html', whatever=whatever)
app.run(debug=True)
