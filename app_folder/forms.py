from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, StringField
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms.fields.html5 import EmailField  
from wtforms import ValidationError

from app_folder import app
from app_folder.models import User, Post

class LoginForm(FlaskForm):
    '''This is the Login Form function

    This function creates a form with username, password, and the ability to remember user.'''
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class DeleteForm(FlaskForm):
      '''This is the delete Form function.

    This function allows the user to delete account.'''

    submit = SubmitField('Yes, delete my account!')
    

class RegisterForm(FlaskForm):
    '''This is the Register Form function.

    This function allows the user to create a form with username, email, and passwords.'''
    username = StringField("Username",validators=[DataRequired(message = "Username is taken.")])
    email = EmailField("Email",validators=[DataRequired("Email is already in use."),Email(message = "Email address must be valid!")])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirmPassword', message = "Passwords Don't Match!")])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register Account')

    def validate_username(self, username):
        '''This function validates the username.
        
        This will check if the username is in the database.'''
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash("Username is taken.")
            raise ValidationError('Username is taken.')
 
    def validate_email(self, email):
        '''This function validates the users email.
        
        This will check if the email is in the database.'''
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash("Email is already in use.")
            raise ValidationError('Email is already in use.')

