from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if 'page_visit_count' in session:
		session['page_visit_count'] += 1
	else:
		session['page_visit_count'] = 1
	return render_template('index.html')


@app.route('/inc_by2')
def inc_by2():
	# only adding one since an additional count will
	# be added in the redirect call
	session['page_visit_count'] += 2
	return render_template('index.html')

@app.route('/reset')
def reset():
	session['page_visit_count'] = 0
	return render_template('index.html')

app.run(debug=True)