from app import app
from flask import render_template

@app.route('/')
@app.route('/Home')
def Home():
	return render_template('Home.html', title="Home Page")
