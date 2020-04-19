from app_folder import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    '''This is the load function .
    
    This function load users'''
    return User.query.get(int(id))
    ''' Return user id'''

class User(UserMixin, db.Model):
    '''This function creates User class.

    This function will create the database for the user.
    Parameters
    id: Integer
        A set of numbers
    username: string
        A name, such as robbin.
    email: string
        A name and ending in @xx.com
    password: string
        A  made up password
     '''
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        '''This function will format username'''
        return '<User {}>'.format(self.username)
        ''' return username '''
       
    def set_password(self, password):
        '''This function will generate a password hash'''
        self.password_hash = generate_password_hash(password)
 
    def check_password(self, password):
        '''This function will check if password is valid'''
        return check_password_hash(self.password_hash, password)
        ''' Check if passwords are the same'''

class Post(db.Model):
    '''This is the post class function.
    
    This function will create the database for the post
    Parameters
    id: Integer
        A set of numbers
    body: string
        creates a database column
    timestamp: date and time
        creates a database column
    user_id: Integer
        creates a database column
        '''
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
 
    def __repr__(self):
        '''This function formats post'''
        return '<Posts {}>'.format(self.body)
        ''' returns post '''
       
