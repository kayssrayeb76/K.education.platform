from app import app
from flask import render_template, redirect, url_for


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.jinja2', title=title)


@app.route('/about')
def about():
    title = 'About'
    return render_template('about.jinja2', title=title)

@app.route('/courses')
def courses():
    title = 'Courses'
    return render_template('courses.jinja2', title=title)

@app.route('/contact')
def contact():
    title = 'Contact'
    return render_template('contact.jinja2', title=title)

@app.route('/sign_in')
def sign_in():
    title = 'Sign In'
    return render_template('sign_in.jinja2', title=title)

@app.route('/sign_up')
def sign_up():
    title = 'Sign Up'
    return render_template('sign_up.jinja2', title=title)