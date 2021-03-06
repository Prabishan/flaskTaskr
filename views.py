import sqlite3
from functools import wraps

from flask import Flask, flash, redirect, render_template, \
    request, session, url_for

#creates an instance of Flask Object
app = Flask(__name__)

#imports all values with Uppercase from file '_config.py'
#and stores it in config object
app.config.from_object('_config') 

def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])

def login_required(test):
    @wraps(test)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args,**kwargs)
        else:
            flash('You need to log in first!')
            return redirect(url_for('login'))
    return wrapper

@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('Goodbye!')
    return redirect(url_for('login'))

@app.route('/' , methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] \
            or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid username or password!'
            return render_template('login.html', error = error)
        else:
            session['loggen_in'] = True
            flash('Welcome')
            return redirect(url_for('tasks'))
    return render_template('login.html')
