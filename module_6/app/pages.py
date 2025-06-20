from flask import Blueprint, render_template

# Create an instance of Blueprint
bp = Blueprint("pages", __name__)

# Define routes to return templates 
@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/contacts")
def contact():
    return render_template("pages/contacts.html")

@bp.route("/projects")
def projects():
    return render_template("pages/projects.html")