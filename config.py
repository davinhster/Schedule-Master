import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    '''Creates Config class.

    This will make a secret key'''
    SECRET_KEY = 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
