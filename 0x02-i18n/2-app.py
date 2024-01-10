#!/usr/bin/env python3
""" Flask API
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFUALT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """ route to home page (index.html)
    """
    return render_template("1-index.html")
