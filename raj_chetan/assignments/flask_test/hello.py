from flask import Flask
from flask import render_template

app = Flask(__name__)  

                                       
@app.route('/')                           
def hello_world():
  return render_template('index.html', name = 'Chetan', times=10)   # Render the template and return it!


@app.route('/success')
def success():
	return render_template('success.html')

@app.route('/another')
def some_function():
	return render_template('another.html')


app.run(debug=True)   