from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ProjectRegistrationForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired()])
    Supervisor1Name = StringField('Primary Supervisor', validators=[DataRequired()])
    submit = SubmitField('Submit Registration')
