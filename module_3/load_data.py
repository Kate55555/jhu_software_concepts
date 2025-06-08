from pathlib import Path
import json
from create_table import create_connection


if __name__ == "__main__":
    app_folder = Path.cwd()

    # Read data from a .json file into a dictionary
    f = open(app_folder / "applicant_data.json", "r")
    file = f.read()
    data = json.loads(file)
    print(f"Loaded data")

    # Establish a connection with the 'gradcafe' database
    connection = create_connection(
        "gradcafe", "postgres", "abc123", "127.0.0.1", "5432"
    )

    # Set up a list of database column names
    table_cols = [
        "program",
        "comments",
        "date_added",
        "url",
        "status",
        "term",
        "us_or_international",
        "gpa",
        "gre",
        "gre_v",
        "gre_aw",
        "degree"
    ]

    cols_sql = ", ".join(table_cols)

    apps = []

    # Get records from the data dictionary
    for datum in data:
        # Extract numeric valuse for GPA-GRE
        if (datum.setdefault("GPA", )):
            gpa = float(datum.setdefault("GPA", None)[3:])
        else:
            gpa = None
        if (datum.setdefault("GRE", None)):
            gre = float(datum.setdefault("GRE", None)[3:])
        else:
            gre = None
        if (datum.setdefault("GRE V", None)):
            gre_v = float(datum.setdefault("GRE V", None)[5:])
        else:
            gre_v = None
        if (datum.setdefault("GRE AW", None)):
            gre_aw = float(datum.setdefault("GRE AW", None)[6:])
        else:
            gre_aw = None

        # Make up a data record
        values = (
            datum.setdefault("program", None),
            datum.setdefault("comments", None),
            datum.get("date_added", None)[9:],
            datum.setdefault("url", None),
            datum.setdefault("status", None),
            datum.setdefault("term", None),
            datum.setdefault("US/Internaional", None),
            gpa,
            gre,
            gre_v,
            gre_aw,
            datum.setdefault("Degree", None)
        )

        # Work around bad data for UIC
        if datum.get("program").find(
                "(UIC), University of Illinois Chicago"
            ) != -1:
            values = (
                datum.setdefault("Degree", None) + ", " + datum.get("program")[7:],
                datum.setdefault("comments", None),
                datum.get("status", None),
                datum.setdefault("url", None),
                None,
                datum.setdefault("term", None),
                datum.setdefault("US/Internaional", None),
                gpa,
                gre,
                gre_v,
                gre_aw,
                datum.get("date_added", None)[9:]
        )

        # Add a tuple with single app info to a list
        apps.append(values)

    # Get a template to add all apps
    app_records = ", ".join(["%s"] * len(apps))

    # Build a query
    insert_query = (
        f"INSERT INTO applicants ({cols_sql}) VALUES {app_records}"
    )

    # Execute and close the database connection
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(insert_query, apps)
    cursor.close()
    connection.close()
    print(f"Inserted data")