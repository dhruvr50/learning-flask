# This is a third python file which could though be integrated directly in routes.py
# Has a functionality significantly different from that of routes.py
# this python file checks the validity of the entered data during sign in before it goes in the database
# we are using Flask extension flask-wtf which helps with creating forms in python as opposed to html
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First Name', validators=[DataRequired("Please enter your first name.")])
	last_name = StringField('Last Name', validators=[DataRequired("Please enter your last name.")])
	email = StringField('Email Id', validators=[DataRequired("Please enter your email id"), Email("Please enter a valid email address.")])
	password = PasswordField('Password', validators=[DataRequired("Please enter  a password"), Length(min=6, message="Please must be 6 characters or more.")])
	submit = SubmitField('Submit It')
