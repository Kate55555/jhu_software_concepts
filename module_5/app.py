"""This module starts a Flask app"""
from src import create_app

# Run the web server
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=True)
