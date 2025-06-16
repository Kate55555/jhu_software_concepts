"""This module queries the database table Applicants"""
from psycopg2 import OperationalError
from create_table import create_connection


def execute_read_query(dbconnection, query):
    """Read data from the database as per the query
    
    :param dbconnection: Connection string
    :type dbconnection: connection
    :param query: Query expression
    :type query: str
    :return: int | float | None
    :rtype: float
    """
    cursor = dbconnection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        return None


def problem_1(dbconnection):
    """Answer the question #1 from the Assignemnt
    
    :param dbconnection: Connection string
    :type dbconnection: connection
    :return: Database entries for Spring 2025
    :rtype: integer
    """
    # 1. How many entries do you have in your database who have applied
    # for Spring 2025?
    select_sp2025 = """
    SELECT
        COUNT(term)
    FROM
        applicants
    WHERE
        term = 'Spring 2025'
    ;"""
    apps_number = execute_read_query(dbconnection, select_sp2025)
    for count in apps_number:
        return count[0]


def problem_2(dbconnection):
    """Answer the question #2 from the Assignemnt
    
    :param dbconnection: Connection string
    :type dbconnection: connection
    :return: Percentage of international students
    :rtype: float
    """
    # 2. What percentage of entries are from international students
    # (not American or Other) (to two decimal places)?
    select_i18n = """
    SELECT
        COUNT(us_or_international)
    FROM
        applicants
    WHERE
        us_or_international <> 'American'
        AND us_or_international <> 'Other'
    UNION
    SELECT
        COUNT(us_or_international)
    FROM
        applicants
    ;"""
    i18n_number = execute_read_query(dbconnection, select_i18n)
    # Compute percentage
    i18n_share = i18n_number[0][0] / i18n_number[1][0] * 100
    return i18n_share


def problem_3(dbconnection):
    """Answer the question #3 from the Assignemnt
    
    :param dbconnection: Connection string
    :type dbconnection: connection
    :return: Average GPA, GRE, GRE V, GRE AW
    :rtype: float
    """
    # 3. What is the average GPA, GRE, GRE V, GRE AW of applicants who
    # provide these metrics?
    select_averages = """
    SELECT
        'Average GPA' AS Category
        ,AVG(gpa) AS Value
    FROM
        applicants
    WHERE
        gpa > 0
        AND gpa <= 4
    UNION
    SELECT
        'Average GRE' AS Category
        ,AVG(gre) AS Value
    FROM
        applicants
    WHERE
        gre >= 130
        AND gre <= 170
    UNION
    SELECT
        'Average GRE V'  AS Category
        ,AVG(gre_v) AS Value
    FROM
        applicants
    WHERE
        gre_v >= 130
        AND gre_v <= 170
    UNION
    SELECT
        'Average GRE AW'  AS Category
        ,AVG(gre_aw) AS Value
    FROM
        applicants
    WHERE
        gre_aw > 0
        AND gre_aw <= 6
    ;"""
    averages = execute_read_query(dbconnection, select_averages)
    return averages


def problem_4(dbconnection):
    """Answer the question #4 from the Assignemnt
    
    :param dbconnection: Connection string
    :type dbconnection: connection
    :return: Average GPA of American students in Spring 2025
    :rtype: float
    """
    # 4. What is their average GPA of American students in Spring 2025?
    select_average = """
    SELECT
        AVG(gpa)
    FROM
        applicants
    WHERE
        gpa > 0
        AND gpa <= 4
        AND us_or_international = 'American'
    ;"""
    average_gpa = execute_read_query(dbconnection, select_average)
    for result in average_gpa:
        return result[0]


def problem_5(dbconnection):
    """Answer the question #5 from the Assignemnt
    
    :param dbconnection: Connection string
    :type dbconnection: connection
    :return: Percentage of accepted applicants for Spring 2025
    :rtype: float
    """
    # 5. What percent of entries for Spring 2025 are Acceptances
    # (to two decimal places)?
    select_accepted = """
    SELECT
        COUNT(status)
    FROM
        applicants
    WHERE
        term = 'Spring 2025'
        AND status LIKE '%Accepted%'
    UNION
    SELECT
        COUNT(status)
    FROM
        applicants
    WHERE
        term = 'Spring 2025'
    ;"""
    accepted = execute_read_query(dbconnection, select_accepted)
    # Compute percentage
    accepted_share = accepted[0][0] / accepted[1][0] * 100
    return accepted_share


def problem_6(dbconnection):
    """Answer the question #6 from the Assignemnt
    
    :param dbconnection: Connection string
    :type dbconnection: connection
    :return: Average GPA of applicants in Spring 2025
    :rtype: float
    """
    # 6. What is the average GPA of applicants who applied for Spring 2025
    # who are Acceptances?
    select_average = """
    SELECT
        AVG(gpa)
    FROM
        applicants
    WHERE
        gpa > 0
        AND gpa <= 4
        AND term = 'Spring 2025'
        AND status LIKE '%Accepted%'
    ;"""
    average_gpa = execute_read_query(dbconnection, select_average)
    for result in average_gpa:
        return result[0]


def problem_7(dbconnection):
    """Answer the question #7 from the Assignemnt
    
    :param dbconnection: Connection string
    :type dbconnection: connection
    :return: Number of entries from applicants who applied to JHU CS
    :rtype: int
    """
    # 7. How many entries are from applicants who applied to JHU for a masters
    # degrees in Computer Science?
    select_jhu = """
    SELECT
        COUNT(program)
    FROM
        applicants
    WHERE
        program LIKE '%Johns Hopkins University%'
        AND program LIKE '%Computer Science%'
        AND degree LIKE '%Masters%'
    ;"""
    jhu_masters_cs = execute_read_query(dbconnection, select_jhu)
    for result in jhu_masters_cs:
        return result[0]


if __name__ == "__main__":
    # Establish a connection with the 'gradcafe' database
    connection = create_connection(
        "gradcafe", "postgres", "abc123", "127.0.0.1", "5432"
    )

    # Problem 1
    print("1. Number of entries for Spring 2025: ")
    print(f"{problem_1(connection)}")

    # Problem 2
    print("2. Entries from international students: ")
    print(f"{problem_2(connection):.2f}%")

    # Problem 3
    print("3. Average GPA, GRE, GRE V, GRE AW: ")
    for score in problem_3(connection):
        print(f"{score[0]}: {score[1]:.2f}")

    # Problem 4
    print("4. Average GPA of American students in Spring 2025: ")
    print(f"{problem_4(connection):.2f}")

    # Problem 5
    print("5. Percent of entries for Spring 2025 that are Acceptances: ")
    print(f"{problem_5(connection):.2f}%")

    # Problem 6
    print("6.  GPA of applicants in Spring 2025 that are accepted: ")
    print(f"{problem_6(connection):.2f}")

    # Problem 7
    print("7. Number of applicants who applied for Masters degrees " \
          "in Computer Science at JHU: ")
    print(f"{problem_7(connection)}")
