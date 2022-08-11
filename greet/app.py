#make a simple Flask app that responds to these routes with simple text
#messages
from flask import Flask
app = Flask(__name__)


#welcome route
@app.route('/welcome')
def get_welcome():
    return f"""
    <h1> This is the welcome page! </h1>
    <p> Welcome to my flask app
    """

@app.route('/welcome/home')
def welcome_home():
    return f"""
    <h1> welcome home!
    """

@app.route('/welcome/back')
def welcome_back():
    return f"""
    <h1> welcome back to the page!
    """

