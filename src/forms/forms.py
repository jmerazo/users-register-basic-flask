from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import EmailField

class UserForm(FlaskForm):
    names = StringField('Names', validators=[DataRequired(), Length(max=64, min=4)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    city = StringField('City', validators=[DataRequired(), Length(min=4, max=50)])
    submit = SubmitField('Save')