import pandas as pd
import sqlite3
import filepaths as fp
import sys
sys.path.append(fp.UTILS_FILEPATH)
import db_operations as db

## Create a test user.

def add_user() -> None:
    """Test by adding a user into userinfo.db."""
    conn = sqlite3.connect('app/databases/userinfo.db')
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS users(username PRIMARY KEY, password TEXT)''')

    user_info = pd.DataFrame({'username': ['Company2'],
                            'password': ['password']})
    data = {'users': user_info}

    db.insert(data, 'app/databases/userinfo.db')

def check_users() -> None:
    """Test to see if it is possible to obtain data from userinfo.db."""

    PROMPT = "SELECT * FROM users"
    conn = sqlite3.connect('app/databases/userinfo.db')
    c = conn.cursor()
    results = c.execute(PROMPT).fetchone()

    assert results == ("Company", "password")

def login_test() -> None:
    """Test to see if logging in is successful."""

    username = 'Company'
    password = 'password'
    db_filepath = 'app/databases/userinfo.db'

    return db.login(username, password, db_filepath)

if __name__ == '__main__':
    add_user()