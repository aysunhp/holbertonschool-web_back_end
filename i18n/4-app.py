#!/usr/bin/env python3
"""
Flask app with forced locale via URL parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Babel configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


def get_locale():
    """
    Determine best locale:
    1. URL parameter (locale)
    2. default fallback
    """
    locale = request.args.get("locale")

    if locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def home():
    """
    Home page
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
