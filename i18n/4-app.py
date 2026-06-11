#!/usr/bin/env python3
"""
<<<<<<< HEAD
Flask app with URL-forced locale support
=======
Flask app with forced locale via URL parameter
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
<<<<<<< HEAD
    Configuration for supported languages and default locale
=======
    Babel configuration
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

<<<<<<< HEAD

def get_locale():
    """
    Determines the best matching language.

    - If 'locale' URL parameter exists and is supported, use it
    - Otherwise, fallback to browser's accepted languages
    """
    locale_param = request.args.get("locale")
    if locale_param in app.config["LANGUAGES"]:
        return locale_param
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)
=======
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
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c


@app.route("/")
def home():
<<<<<<< HEAD
    """Render the home page"""
    return render_template("4-index.html")
=======
    """
    Home page
    """
    return render_template("3-index.html")
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c


if __name__ == "__main__":
    app.run(debug=True)
