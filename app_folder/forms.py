from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, StringField, TimeField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email, NumberRange
from wtforms.fields.html5 import EmailField

from app_folder import app
from app_folder.models import User, Post

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class DeleteForm(FlaskForm):
    submit = SubmitField('Yes, delete my account!')

class RegisterForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired(message = "Username is taken.")])
    email = EmailField("Email",validators=[DataRequired("Email is already in use."),Email(message = "Email address must be valid!")])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirmPassword', message = "Passwords Don't Match!")])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register Account')

    def validate_username(self, username):
        ''' This function validates the username. This will check if the username is in the database.

            Args:
                username (string) : The username of the user.
        '''
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash("Username is taken.")
            raise ValidationError('Username is taken.')

    def validate_email(self, email):
        ''' This function validates the users email. This will check if the email is in the database.

            Args:
                email (string) : Is the user's email
        '''
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash("Email is already in use.")
            raise ValidationError('Email is already in use.')

class AvailabilityForm(FlaskForm):
    startTime = TimeField("Start",validators=[DataRequired(),NumberRange(min=1, max=12, message='Select a range between 9 AM and 12 PM')])
    endTime = TimeField("End",validators=[DataRequired(),NumberRange(min=1, max=12, message='Select a range between 9 AM and 12 PM')])
    submit = SubmitField('Set Availability')

class SettingsForm(FlaskForm):
    meetingLength = SelectField('Meeting Length: ',choices=[('60', '60 minutes'), ('30', '30 minutes'), ('15', '15 minutes')])
    emailConfirmation = BooleanField("Email Confirmation")
    submit = SubmitField('Update Settings')