#!/usr/bin/env python3
"""Basic Flask application"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def hello_world():
   """Route that returns a template"""
   return render_template('0-index.html')