from app_folder import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    ''' This is the load function that loads users

        Args:
            id (int) : The users id from the database.

        Returns:
            Will return the user with ID number id.
    '''
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    emailConfirmation = db.Column(db.String(2), index=True)
    meetingLength = db.Column(db.String(32), index=True)
    availabilityStart = db.Column(db.String(32),index = True)
    availabilityEnd = db.Column(db.String(32),index = True)

    posts = db.relationship('Post', backref='author', lazy='dynamic')


    def __repr__(self):
        ''' This function will format username
        
            Returns:
                Will return a username.
        '''
        return '<User {}>'.format(self.username)
       
    def set_password(self, password):
        ''' This function will generate a password hash.

            Args:
                password (string) : The user's password
        '''
        self.password_hash = generate_password_hash(password)
 
    def check_password(self, password):
        ''' This function will check if password is valid
        
            Args:
                password (string) : The user's password

            Returns:
                Will return true or false depending on if the password is valid.
        '''
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
 
    def __repr__(self):
        ''' This function formats post.

            Returns:
                Will return a format.
        '''
        return '<Posts {}>'.format(self.body)
       
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    eventDate = db.Column(db.String(32), index=True)
    eventTime = db.Column(db.String(32), index=True)
    militaryTime = db.Column(db.String(32), index=True)
    guestname = db.Column(db.String(64), index=True)
    description = db.Column(db.String(128), index=True)

    def __repr__(self):
        ''' This function will format username
        
            Returns:
                Will return a username.
        '''
        return '<User {}>'.format(self.username)