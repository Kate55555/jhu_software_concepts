import psycopg2
from flask import Blueprint, render_template
import query_data

# Create an instance of Blueprint
bp = Blueprint("pages", __name__)

def get_db_connection():
    """A function to connect to the database"""
    connection = psycopg2.connect(
        dbname="gradcafe",
        user="postgres",
        password="abc123", 
        host="127.0.0.1", 
        port="5432"
    )
    return connection


# Define routes to return templates 
@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/analysis")
def analysis():
    conn = get_db_connection()
    cur = conn.cursor()
    answers = {
        "P1": query_data.problem_1(conn),
        "P2": query_data.problem_2(conn),
        "P3": query_data.problem_3(conn),
        "P4": query_data.problem_4(conn),
        "P5": query_data.problem_5(conn),
        "P6": query_data.problem_6(conn),
        "P7": query_data.problem_7(conn)
    }
    cur.close()
    conn.close()

    return render_template("pages/analysis.html", answers=answers)