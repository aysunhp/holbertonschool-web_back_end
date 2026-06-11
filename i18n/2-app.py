#!/usr/bin/env python3
<<<<<<< HEAD
"""
Flask-Babel
"""
from flask import Flask, request, render_template
=======
""" Flask  Babel application"""

from flask import Flask, render_template
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
from flask_babel import Babel


app = Flask(__name__)


<<<<<<< HEAD
def get_locale():
    """Determines the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(locale_selector=get_locale)
babel.init_app(app)


@app.route("/")
def home():
    """Route that returns a template"""
    return render_template('2-index.html')
=======
class Config(object):
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """Select a language translation to use for the request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def hello_world():
    """Route that returns a template"""
    return render_template('0-index.html')
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
