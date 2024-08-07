import pandas as pd
import datetime
import sqlite3
from llm.predibase_sentiment import PredibaseSentiment
import app.utils.db_operations as db

def transform(data: dict, analyzer: PredibaseSentiment) -> pd.DataFrame:
    """Take in piece of data and an analyzer and process the data.
    
    Attributes:
        dict: Dictionary of data.
        analyzer: PredibaseSentiment sentiment analyzer.
    """

    return analyzer.sentiment(data)

def load(data: pd.DataFrame, database: str) -> None:
    """Take in a piece of data in dataframe form and load it into a database.

    Attributes:
        data: A Pandas Dataframe of data.
        database: The database name.
    
    """

    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS feedbacks(id PRIMARY KEY, feedback TEXT, community VARCHAR(50), category VARCHAR(50), time DATETIME, sentiment INT)''')

    data = {'feedbacks': data}

    db.insert(data, database)

def etl(data: dict, database: str, analyzer: PredibaseSentiment) -> None:
    """Take in a piece of data, a database and an analyzer and perform ETL.
    
    Attributes:
        data: A dictionary of data.
        database: Database Filepath
        analyzer: Analyzer of Sentiment (PredibaseSentiment)
    """

    data = transform(data, analyzer)
    print(data)
    load(data, database)
    