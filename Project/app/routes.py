from app import app, db
from app.forms import ProjectRegistrationForm
from app.models import ProjectRegistrationModel
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/Home')
def Home():
	return render_template('Home.html')

@app.route('/Undergraduate')
def Undergraduate():
	return render_template('Undergraduate.html')

@app.route('/ProjectRegistration', methods=['GET', 'POST'])
def ProjectRegistration():
	form = ProjectRegistrationForm()
	if form.validate_on_submit():
		ProjectRegistrationDetails = ProjectRegistrationModel(
		title = form.title.data,
		Supervisor1Name = form.Supervisor1Name.data
		)
		db.session.add(ProjectRegistrationDetails)
		db.session.commit()
		return redirect(url_for('Home'))
	return render_template('ProjectRegistration.html', form = form)

@app.route('/ProjectList')
def ProjectList():
	projects = db.session.query(ProjectRegistrationModel).all()
	return render_template('ProjectList.html', projects = projects)
