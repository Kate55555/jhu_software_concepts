"""This module defines routes of the Flask application"""
from flask import Blueprint, render_template

# Create an instance of Blueprint
bp = Blueprint("pages", __name__)

# Define routes to return templates
@bp.route("/")
def home():
    """Define what the home page returns"""
    return render_template("pages/home.html")

@bp.route("/contacts")
def contact():
    """Define what the contacts page returns"""
    return render_template("pages/contacts.html")

@bp.route("/projects")
def projects():
    """Define what the projects page returns"""
    return render_template("pages/projects.html")
