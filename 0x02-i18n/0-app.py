#!/usr/bin/env python3
""" Flask API
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """ route to home page (index.html)
    """
    return render_template("0-index.html")
