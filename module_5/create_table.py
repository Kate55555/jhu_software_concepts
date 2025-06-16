"""This module creates a table Applicants within the Gradcafe database"""
import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    """Make a connection with a PostgreSQL database"""
    dbconnection = None
    try:
        dbconnection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return dbconnection


def create_database(dbconnection, query):
    """Create a new database in the PostgreSQL database server"""
    dbconnection.autocommit = True
    cursor = dbconnection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def execute_query(dbconnection, query):
    """Execute Python SQL queries on the PostgreSQL database"""
    dbconnection.autocommit = True
    cursor = dbconnection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


if __name__ == "__main__":
    # Create a connection to the default PostgreSQL database
    connection = create_connection(
        "postgres", "postgres", "abc123", "127.0.0.1", "5432"
    )

    # Create a new database 'gradcafe' in the PostgreSQL database server
    CREATE_DATABASE_QUERY = "CREATE DATABASE gradcafe"
    create_database(connection, CREATE_DATABASE_QUERY)

    # Establish a connection with the 'gradcafe' database
    connection = create_connection(
        "gradcafe", "postgres", "abc123", "127.0.0.1", "5432"
    )

    # Create the table 'applicants' inside the 'gradcafe' database
    CREATE_APPLICANTS_TABLE = """
    CREATE TABLE IF NOT EXISTS applicants (
        p_id SERIAL PRIMARY KEY,
        program TEXT NOT NULL,
        comments TEXT,
        date_added DATE,
        url TEXT,
        status TEXT,
        term TEXT,
        us_or_international TEXT,
        gpa FLOAT,
        gre FLOAT,
        gre_v FLOAT,
        gre_aw FLOAT,
        degree TEXT
    )
    """
    execute_query(connection, CREATE_APPLICANTS_TABLE)
