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


@app.route("/")
def index():
    """ route to home page (index.html)
    """
    return render_template("1-index.html")
