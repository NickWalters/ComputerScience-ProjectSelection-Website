from app import app
from app.forms import ProjectRegistrationForm
from flask import render_template

@app.route('/')
@app.route('/Home')
def Home():
	return render_template('Home.html')

@app.route('/Undergraduate')
def Undergraduate():
	return render_template('Undergraduate.html')

@app.route('/ProjectRegistration')
def ProjectRegistration():
	form = ProjectRegistrationForm()
	return render_template('ProjectRegistration.html', form = form)
