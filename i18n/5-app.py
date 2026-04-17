#!/usr/bin/env python3
"""
Flask app with mock login and Babel support
"""

from flask import Flask, request, render_template, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """
    Return user or None
    """
    if login_as is None:
        return None
    return users.get(login_as)


@app.before_request
def before_request():
    """
    Finds a user if login_as exists in the request and assigns it
    to flask.g.user for global access during the request lifecycle.
    """
    login_as = request.args.get("login_as", type=int)
    g.user = get_user(login_as)

    # DEBUG
    print("LOGIN_AS:", login_as)
    print("USER:", g.user)


def get_locale():
    """
    Locale selection priority:
    1. URL param
    2. user settings
    3. browser headers
    """
    locale = request.args.get("locale")

    if locale in app.config["LANGUAGES"]:
        return locale

    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user.get("locale")

    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def home():
    """
    Home page
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
