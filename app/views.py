from flask import render_template
from app import app
from flask_bootstrap import Bootstrap

# Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     return render_template('index.html')

# Views
@app.route('/')

def index():
    
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to News Updates'
    return render_template('index.html', title = title)