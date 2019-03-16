"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect, url_for
import app
from forms import LoginForm

@app.app.route('/')
@app.app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        app_name='Test App'
    )

@app.app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.',
        app_name='Test App'
    )

@app.app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.',
        app_name='Test App'
    )

@app.app.route('/login', methods=['GET', 'POST'])
def login():
    """Renders the login page."""
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        app_name='Test App',
        form=form
    )