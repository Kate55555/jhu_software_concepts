import json
from create_table import create_connection, execute_query


if __name__ == "__main__":
    # Read data from a .json file into a dictionary
    f = open("module_3/applicant_data.json", "r")
    file = f.read()
    data = json.loads(file)
    print(f"Loaded data")

    # Establish a connection with the 'gradcafe' database
    connection = create_connection(
        "gradcafe", "postgres", "abc123", "127.0.0.1", "5432"
    )

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

        if (datum.get("program").find("(UIC), University of Illinois Chicago") != -1):
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
            
        apps.append(values)
    
    app_records = ", ".join(["%s"] * len(apps))

    insert_query = (
        f"INSERT INTO applicants ({cols_sql}) VALUES {app_records}"
    )

    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(insert_query, apps)
    cursor.close()
    connection.close()
    print(f"Inserted data")