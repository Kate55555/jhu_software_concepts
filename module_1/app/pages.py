from flask import Blueprint, render_template, request

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/contacts")
def contact():
    return render_template("pages/contacts.html")

@bp.route("/projects")
def projects():
    return render_template("pages/projects.html")