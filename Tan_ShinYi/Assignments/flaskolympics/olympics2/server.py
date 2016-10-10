from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def myfirstfunction():
    return render_template('index.html', name="Mike")

if __name__ == '__main__':
  app.run(debug = True)
