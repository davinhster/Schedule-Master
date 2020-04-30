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
    startTime = SelectField('Start: ',choices=[
        ('9', '9 AM'),
        ('9.25', '9:15 AM'),
        ('9.5', '9:30 AM'),
        ('9.75','9:45 AM'),
        ('10','10:00 AM'),
        ('10.25','10:15 AM'),
        ('10.5','10:30 AM'),
        ('10.75','10:45 AM'),
        ('11','11:00 AM'),
        ('11.25','11:15 AM'),
        ('11.5','11:30 AM'),
        ('11.75','11:45 AM'),
        ('12','12:00 PM'),
        ('12.25','12:15 PM'),
        ('12.5','12:30 PM'),
        ('12.75','12:45 PM'),
        ('13','1:00 PM'),
        ('13.25','1:15 PM'),
        ('13.5','1:30 PM'),
        ('13.75','1:45 PM'),
        ('14','2:00 PM'),
        ('14.25','2:15 PM'),
        ('14.5','2:30 PM'),
        ('14.75','2:45 PM'),
        ('15','3:00 PM'),
        ('15.25','3:15 PM'),
        ('15.5','3:30 PM'),
        ('15.75','3:45 PM'),
        ('16','4:00 PM'),
        ('16.25','4:15 PM'),
        ('16.5','4:30 PM'),
        ('16.75','4:45 PM'),
        ('17','5:00 PM'),
        ('17.25','5:15 PM'),
        ('17.5','5:30 PM'),
        ('17.75','5:45 PM'),
        ('18','6:00 PM'),
        ('18.25','6:15 PM'),
        ('18.5','6:30 PM'),
        ('18.75','6:45 PM'),
        ('19','7:00 PM'),
        ('19.25','7:15 PM'),
        ('19.5','7:30 PM'),
        ('19.75','7:45 PM'),
        ('20','8:00 PM'),
        ('20.25','8:15 PM'),
        ('20.5','8:30 PM'),
        ('20.75','8:45 PM'),
        ('21','9:00 PM'),
        ('21.25','9:15 PM'),
        ('21.5','9:30 PM'),
        ('21.75','9:45 PM')])
    endTime = SelectField('End: ',choices=[
        ('9.25', '9:15 AM'),
        ('9.5', '9:30 AM'),
        ('9.75','9:45 AM'),
        ('10','10:00 AM'),
        ('10.25','10:15 AM'),
        ('10.5','10:30 AM'),
        ('10.75','10:45 AM'),
        ('11','11:00 AM'),
        ('11.25','11:15 AM'),
        ('11.5','11:30 AM'),
        ('11.75','11:45 AM'),
        ('12','12:00 PM'),
        ('12.25','12:15 PM'),
        ('12.5','12:30 PM'),
        ('12.75','12:45 PM'),
        ('13','1:00 PM'),
        ('13.25','1:15 PM'),
        ('13.5','1:30 PM'),
        ('13.75','1:45 PM'),
        ('14','2:00 PM'),
        ('14.25','2:15 PM'),
        ('14.5','2:30 PM'),
        ('14.75','2:45 PM'),
        ('15','3:00 PM'),
        ('15.25','3:15 PM'),
        ('15.5','3:30 PM'),
        ('15.75','3:45 PM'),
        ('16','4:00 PM'),
        ('16.25','4:15 PM'),
        ('16.5','4:30 PM'),
        ('16.75','4:45 PM'),
        ('17','5:00 PM'),
        ('17.25','5:15 PM'),
        ('17.5','5:30 PM'),
        ('17.75','5:45 PM'),
        ('18','6:00 PM'),
        ('18.25','6:15 PM'),
        ('18.5','6:30 PM'),
        ('18.75','6:45 PM'),
        ('19','7:00 PM'),
        ('19.25','7:15 PM'),
        ('19.5','7:30 PM'),
        ('19.75','7:45 PM'),
        ('20','8:00 PM'),
        ('20.25','8:15 PM'),
        ('20.5','8:30 PM'),
        ('20.75','8:45 PM'),
        ('21','9:00 PM'),
        ('21.25','9:15 PM'),
        ('21.5','9:30 PM'),
        ('21.75','9:45 PM'),
        ('22','10:00 PM')])
    submit = SubmitField('Set Availability')

class SettingsForm(FlaskForm):
    meetingLength = SelectField('Meeting Length: ',choices=[('60', '60 minutes'), ('30', '30 minutes'), ('15', '15 minutes')])
    emailConfirmation = BooleanField("Email Confirmation")
    submit = SubmitField('Update Settings')