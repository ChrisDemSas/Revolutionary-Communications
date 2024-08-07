import pandas as pd
import sqlite3
import sys
import etl
from llm.predibase_sentiment import *

def test_etl(data: dict) -> None:
    """Tests the ETL Pipeline."""

    API_TOKEN = ''
    database = 'app/databases/feedback.db'

    predibase = PredibaseSentiment(API_TOKEN, 'review-sentiment-model/3')
    etl.etl(data, database, predibase)

    return "Success!"

if __name__ == '__main__':

    feedback = [('The tour group was very disrespectful.', 'Miscellaneous'), 
                ('The tour group was littering everywhere. Even the beaches are full of trash!', 'Environment'),
                ('I saw a tour group try to feed animals, that is wrong.', 'Environment'), 
                ('The tour guide failed to brief the tourists on our customs.', 'Culture'),
                ('The tourists were very rude. Do better!', 'Miscellaneous')
                ]
    
    for index, f in enumerate(feedback):
        data = {
        'id': index,
        'community': 'Haenyo',
        'category': f[1],
        'time': datetime.datetime.now(),
        'feedback': f[0],
    }

        test = test_etl(data)
        print(test)