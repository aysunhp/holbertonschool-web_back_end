#!/usr/bin/env python3
"""
<<<<<<< HEAD
This module is for Babel object instantiation
"""
=======
Flask app with mock login and Babel support
"""

>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
from flask import Flask, request, render_template, g
from flask_babel import Babel


<<<<<<< HEAD
class Config:
    """
    This class is for configuring the languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale():
    """
    Determines the best match for supported languages
    """
    if request.args.get('locale'):
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])
=======
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
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """
<<<<<<< HEAD
    Returns a user dictionary or None if the ID cannot be found
    """
    if login_as is None:
        return None
    if login_as not in users:
        return None
    return users.get(login_as)


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.before_request
def before_request():
    """
    Finds a user if any, and sets it as a global on flask.g.user
    """
    login_as = request.args.get('login_as', type=int)
    g.user = get_user(login_as)


@app.route('/')
def home():
    """
    Renders the template
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
=======
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
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
