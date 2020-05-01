from flask import render_template, redirect, flash, request
from app_folder import app, db, login
from .forms import LoginForm, RegisterForm, DeleteForm, AvailabilityForm, SettingsForm
from app_folder.models import User, Post
from flask_login import current_user, login_required, logout_user, login_user
import calendar
import datetime
import numpy

# different URL the app will implement
@app.route("/")
@login_required
def hello():
    ''' This function will greet the user. This function welcomes the user with their username after they login.

        Returns:
            Will render the index page A.K.A. home page.
    '''
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' This is the Login function. This function checks if username and password is valid.
        
        Returns:
            Will redirect to the home page or login page depending on the flow of logic.
    '''
    if current_user.is_authenticated:
        return redirect("/")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect("login")
        login_user(user, remember=form.remember_me.data)
        return redirect("/")
    return render_template('login.html', title='Sign In', form=form)
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    ''' This is the Register function.

        Returns:
            Will redirect to the home page, login page, or registration page depending of the flow of logic.
    '''
    if current_user.is_authenticated:
        return redirect("/")
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, your account has been created!')
        return redirect('login')
    return render_template('register.html', title='Register', form=form)
    

@app.route('/logout')
@login_required
def logout():
    ''' This is the Logout function. This function will logout the user and will not allow access to any info.

        Returns:
            Will redirect to the home page.
    '''
    logout_user()
    return redirect("home")

@app.route('/delete', methods = ['GET','POST'])
@login_required
def delete_account():
    ''' This is the delete account function.
    
        Returns:
            Will redirect to home or delete account page based on the flow of logic.
    '''
    form = DeleteForm()
    if form.validate_on_submit():
        if "cancel_button" in request.form:
            return redirect("settings")
        else:
            user = current_user
            db.session.delete(user)
            db.session.commit()
            flash('Sorry to see you go.')
            return redirect("home")
    return render_template('delete.html', title = 'Delete Account',form = form)
    

@app.route('/goodbye',methods = ['GET','POST'])
def goodbye():
    ''' This function brings the former user to a farewell page.
    
        Returns:
            Will redirect the user to the goodbye page.
    '''
    return render_template('goodbye.html',title = "Goodbye")
    
@app.route('/viewEvents')
@login_required
def viewEvents():
    ''' This is the veiwEvents function.
    
        Returns:
            Will redirect the user to the view events page.
    '''
    return render_template('viewEvents.html', title='View Events')
    
   
@app.route('/settings', methods = ['GET','POST'])
@login_required
def settings(): 
    ''' This is the settings function.
    
        Returns:
            Will redirect the user to the settings page.
    '''
    form = SettingsForm()
    if form.validate_on_submit():
        meetingLength = form.meetingLength.data
        emailConfirmation = form.emailConfirmation.data

        user = current_user
        user.meetingLength = str(meetingLength)
        user.emailConfirmation = str(emailConfirmation)
        db.session.commit()
        
        flash("Settings Updated")
    return render_template('settings.html', title='settings', form = form)

@app.route("/booktime/<user>/<day>-<month>-<year>")
def bookTime(user,day,month,year):
    ''' This is the book time function for guests.
    
        Returns:
            This will redirect the guest to the book times page.
    '''
    theUser = User.query.filter_by(username=user).first()
    timeInterval = float(theUser.meetingLength) / 60.0
    start = float(theUser.availabilityStart)
    end = float(theUser.availabilityEnd)
    theRange = numpy.arange(start,end,timeInterval)
    return render_template('booktime.html', title='Book Time',theInterval = timeInterval, range = theRange) 

@app.route("/home")
def home():
    ''' This is the home function for guests.
    
        Returns:
            This will redirect the guest home.
    '''
    return render_template('home.html', title='home') 

@app.route("/schedule-meeting/<user>")
def scheduleMeeting(user):
    ''' This is the home function for guests.
    
        Returns:
            This will redirect the guest schedule page for a specified user.
            If the specified user doesn't exits it will return "Page not found"
    '''
    theUser = User.query.filter_by(username=user).first()
    if(theUser is not None):
        return render_template('scheduleMeeting.html', title='Schedule',aUser = theUser,calendar = calendar,datetime = datetime)
    else:
        return render_template('pageNotFound.html', title='Nonexistant Page')

@app.route("/addavailability", methods = ['GET','POST'])
@login_required
def add_availability():
    ''' This is the add availability function.
    
        Returns:
            This will redirect the user to the add availability page.
    '''

    form = AvailabilityForm()
    if form.validate_on_submit():
        start = form.startTime.data
        end = form.endTime.data
        user = current_user
        user.availabilityStart = str(start)
        user.availabilityEnd = str(end)
        db.session.commit()
        flash('Availability Range Updated')
        return redirect("settings")   
    return render_template('addAvailability.html', title='Add Availability',form = form) 

@app.route("/users")
def users():
    ''' Lists all the users in the database to select an event from
    

        Returns:
            a list of users to choose events from

    '''

    userList = User.query.all()

    return render_template('users.html',title ='List of Users',userList = userList)


@app.route("/resetpassword")
@login_required
def reset_password():
    ''' This is the reset password function.
    
        Returns:
            This will redirect the user to the reset password page.
    '''
    return render_template('resetPassword.html', title='Reset Password')  
