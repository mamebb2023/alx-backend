#!/usr/bin/env python3
""" Flask App
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Union, Dict


class Config:
    """ Config class
    """

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """ Retrive a user based on login_as
    """
    user = request.args.get('login_as')
    if user:
        return users.get(int(user))
    return None


@app.before_request
def before_request():
    """ Execute before any function
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """ Retrive the language
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ Default route
    """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run()
