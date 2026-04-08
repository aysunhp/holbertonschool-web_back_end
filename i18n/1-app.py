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


@app.route("/")
def hello_world():
    """Route that returns a template"""
    return render_template('0-index.html')
