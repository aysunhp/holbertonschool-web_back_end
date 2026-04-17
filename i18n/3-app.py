#!/usr/bin/env python3
"""
Basic Flask app with Babel internationalization
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Babel config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


def get_locale():
    """
    Get locale from URL parameter
    """
    return request.args.get("locale", "en")


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def home():
    """
    Home page
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
