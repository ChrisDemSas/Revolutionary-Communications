import sqlite3
import pandas as pd

def login(username: str, password: str, database: str) -> str:
    """Take in a database filepath and return 'Authenticated' if logging in was successful.
    
    Attributes:
        username: The username of the company.
        password: The password of the company.
        database: Filepath for the database.
    
    Pre-Condition: Must have users table and from the user login database.
    """

    QUERY = f"""SELECT password
    FROM users 
    WHERE username = '{username}'
    """

    con = sqlite3.connect(database)
    result_password = con.execute(QUERY).fetchone()[0]

    if password == result_password:
        return 'Authenticated'
    else:
        return 'Authentication Failed'

def insert(data: dict, database: str) -> None:
    """Take in a table, a row and a database and insert it into a database.
    Create a table if it doesn't exist.
    
    Attributes:
        data: The dataset in dictionary format, with table name and dataframe object {table name: data}.
        database: Database filepath.
    """

    conn = sqlite3.connect(database)

    for item in data:
        curr = data[item]
        curr.to_sql(item, con = conn, if_exists = 'append', index = False)
    
    conn.commit()
    conn.close()