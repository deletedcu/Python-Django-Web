from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/')
def main_page():
    return render_template('landing_page.html', name='Gangstaz')

@app.route('/ninjas')
def ninjas_page():
    return render_template('ninjas.html', ninjas='Ninjas', answer='He gives it to others!')

@app.route('/dojos/new')
def dojos_page():
    return render_template('dojos.html')

app.run(debug=True)
