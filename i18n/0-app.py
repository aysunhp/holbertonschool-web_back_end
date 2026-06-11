#!/usr/bin/env python3
"""Basic Flask application"""

from flask import Flask, render_template

<<<<<<< HEAD

=======
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
app = Flask(__name__)


@app.route("/")
<<<<<<< HEAD
def home():
=======
def hello_world():
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
    """Route that returns a template"""
    return render_template('0-index.html')
