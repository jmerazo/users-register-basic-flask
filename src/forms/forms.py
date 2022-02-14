from email import message
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, TextField
from wtforms.validators import DataRequired, Email, InputRequired
from wtforms.fields.html5 import EmailField
from wtforms import validators

class UserForm(FlaskForm):
    names = StringField('Names', 
                        [ 
                          validators.length(min=4, max=60, message='Input your name'), 
                          validators.Required(message = 'Names is required')
                        ])
    email = EmailField('Email',  
                        [
                          validators.Email(message='Input email validate'),
                          validators.Required(message='Email is required')
                        ])
    city = StringField('City', 
                        [ 
                          validators.length(min=4, max=40, message='Input city'), 
                          validators.Required(message = 'City is required')
                        ])
    submit = SubmitField('Save')