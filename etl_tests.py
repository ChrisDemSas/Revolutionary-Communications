import pandas as pd
import sqlite3
import sys
import etl
from llm.predibase_sentiment import *

def test_etl() -> None:
    """Tests the ETL Pipeline."""

    API_TOKEN = 'pb_2lVSWVmcVQGkFuKPuQDvIQ'
    database = 'app/databases/feedback.db'

    data = {
        'id': [1],
        'feedback': ['The tour group was very disrespectful to our culture.'],
        'time': [datetime.datetime.now()],
        'category': ['culture']
    }

    predibase = PredibaseSentiment(API_TOKEN, 'review-sentiment-model/3')
    etl.etl(data, database, predibase)

    return "Success!"

if __name__ == '__main__':

    test = test_etl()
    print(test)