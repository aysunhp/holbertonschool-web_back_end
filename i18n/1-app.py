#!/usr/bin/env python3
<<<<<<< HEAD
"""
Flask-Babel
"""
=======
""" Flask  Babel application"""

>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
<<<<<<< HEAD
def home():
    """Route that returns a template"""
    return render_template('1-index.html')
=======
def hello_world():
    """Route that returns a template"""
    return render_template('0-index.html')
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
