#!/usr/bin/env python3
"""
Flask app with user locale priority and Babel support.
"""

from flask import Flask, request, render_template, g
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Configures available languages and default locale/timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


# Mock users
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as: int) -> dict | None:
    """
    Returns a user dictionary based on login_as ID or None if not found.
    """
    if login_as is None:
        return None
    return users.get(login_as)


@app.before_request
def before_request() -> None:
    """
    Retrieves a user from the request and stores it in flask.g.user.
    """
    login_as = request.args.get("login_as", type=int)
    g.user = get_user(login_as)


def get_locale() -> str:
    """
    Determines the best locale based on:
    1. URL parameter
    2. User preferred locale
    3. Request headers
    4. Default locale
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    if g.user:
        user_locale = g.user.get("locale")
        if user_locale in app.config["LANGUAGES"]:
            return user_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def home() -> str:
    """
    Renders the home page template.
    """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(debug=True)