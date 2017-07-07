from flask_wtf import Form 
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class ContactMeForm(Form):
	name = StringField('name', validators=[DataRequired()])
	comment = StringField('comment', validators=[DataRequired()])