#!/usr/bin/env python3
""" Flask  Babel application"""

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


def get_locale():
    """Select a language translation to use for the request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def hello_world():
    """Route that returns a template"""
    return render_template('0-index.html')
