from flask import Flask, render_template, request, url_for, flash, redirect

import binascii

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bc3d60083b40d113ebfc1871676cf648be4767ee74a6eb5a'

formDict = []

#Crear un entorno virtual de python:
#1º)python3 -m venv venv
#Activarlo: source venv/bin/activate
#Desactivarlo: deactivate

@app.route('/', methods=('GET', 'POST'))
def index():
	if request.method == 'POST':
		PIN = request.form['PIN']
		name = request.form['name']
		if not PIN:
			flash('PIN is required!')
		elif not name:
			flash('Name is required!')
		else:
			formDict.clear()
			formDict.append({'PIN': PIN, 'name': name})
			return redirect(url_for('authentication'))
	return render_template('index.html')

@app.route('/authentication')
def authentication():

	print(str(formDict[0]['PIN']))
	print("Login successful")

	name = formDict[0]['name']
	
	print("User entered the following message: " + name)	

	print("Welcome back " + name)

	return render_template('authentication.html', name=name)

if __name__ == "__main__":
	index()
	app.run(host="127.0.0.1", port=8080, debug=True)
