from flask import Flask

from app import pages

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Connect the 'pages' Blueprint with the Flask application
    app.register_blueprint(pages.bp)
    
    return app