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
    FROM user 
    WHERE username = {username}
    """

    con = sqlite3.connect(database)
    result = con.execute(QUERY)

    return result

def insert(data: dict, database: str) -> None:
    """Take in a table, a row and a database and insert it into a database.
    Create a table if it doesn't exist.
    
    Attributes:
        data: The dataset in dictionary format, with title and dataframe object {title: data}.
        row: The row of data to be added, in this format: 
    """

    conn = sqlite3.connect(database)

    for item in data:
        curr = data[item]
        curr.to_sql(item, con = conn, if_exists = 'append', index = False)





