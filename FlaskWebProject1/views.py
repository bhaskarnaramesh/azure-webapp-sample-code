"""
Routes and views for the flask application.
"""

from FlaskWebProject1 import app

@app.route('/')
def home():
    """Renders the home page."""
    return "Hello, Flask!"