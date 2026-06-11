#!/usr/bin/env python3
"""
Basic Flask app with Babel internationalization
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
<<<<<<< HEAD
    Configuration class for Babel settings
=======
    Babel config
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

<<<<<<< HEAD

def get_locale():
    """
    Select the best matching language from the request
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)
=======
babel = Babel(app)


def get_locale():
    """
    Get locale from URL parameter
    """
    return request.args.get("locale", "en")


babel.init_app(app, locale_selector=get_locale)
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c


@app.route("/")
def home():
    """
<<<<<<< HEAD
    Render the home page
=======
    Home page
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
