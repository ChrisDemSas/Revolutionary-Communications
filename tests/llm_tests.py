import pandas as pd
import sqlite3
import filepaths as fp
import sys
sys.path.append(fp.PREDIBASE_FILEPATH)
from predibase_sentiment import PredibaseSentiment
import datetime

def test_predibase() -> pd.DataFrame:
    """Tests a predibase instance to create a sentiment."""

    API_TOKEN = ''

    data = {
        'feedback': ['The tour group was very disrespectful to our culture.'],
        'time': [datetime.datetime.now()],
        'category': ['culture']
    }

    predibase = PredibaseSentiment(API_TOKEN, 
                          'review-sentiment-model/3')

    data = predibase.sentiment(data)

    return data

if __name__ == '__main__':
    data = test_predibase()

    print(data)