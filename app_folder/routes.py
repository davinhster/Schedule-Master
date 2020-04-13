from flask import render_template
from flask import redirect
from flask import flash
from app_folder import app, db
from .forms import LoginForm, RegisterForm
from app_folder.models import User, Post

# different URL the app will implement
@app.route("/")
# called view function
def hello():
    user_dictionary = {'username': 'Miguel'}
    posts_list = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user_dictionary, posts=posts_list)

@app.route('/login', methods=['GET', 'POST'])
def login():
    current_form = LoginForm()
    if current_form.validate_on_submit():
        flash(f'Login requested for user {current_form.username.data}')
        return redirect('/')
    return render_template('login.html', title='Sign In', form=current_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    current_form = RegisterForm()
    if current_form.validate_on_submit():
        user = User(current_form.username,current_form.email)
        db.session.add(user)
        db.session.commit()
        
        return redirect('/')
    return render_template('register.html', title='Register', form=current_form)