from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms.fields.html5 import EmailField  

from app_folder import app
from app_folder.models import User, Post
 
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    email = EmailField("Email",validators=[DataRequired(),Email(message = "Email address must be valid!")])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirmPassword', message = "Passwords Don't Match!")])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register Account')

    def validate_username(self, username):
        '''This function will validate username.'''
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username is taken.')
 
    def validate_email(self, email):
        '''This function will validate email.'''
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email is already in use.')
