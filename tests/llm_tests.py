import pandas as pd
import sqlite3
import filepaths as fp
import sys
sys.path.append(fp.PREDIBASE_FILEPATH)
from predibase_sentiment import PredibaseSentiment
from solar import Solar
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

def test_solar():
    """Tests Solar LLM."""

    API_TOKEN = 'up_SpqVIaeXxeM9uf8yUWxPkUUHJ2vpZ'
    client = Solar(API_TOKEN)

if __name__ == '__main__':
    """
    API_TOKEN = ''
    client = Solar(API_TOKEN)
    verdict = True

    while verdict:
        message = input('Type Message Here:')
        response = client.message(message)
        print(response)

        if message == 'bye':
            verdict = False
    """
