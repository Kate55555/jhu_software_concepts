"""This module creates a Flask app blueprint"""
from flask import Flask

from src import pages

def create_app():
    """Create a Flask application instance
    
    :return: None
    :rtype: None
    """
    app = Flask(__name__)

    # Connect the 'pages' Blueprint with the Flask application
    app.register_blueprint(pages.bp)

    return app
