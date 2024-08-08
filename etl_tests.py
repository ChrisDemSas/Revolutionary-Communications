import pandas as pd
import sqlite3
import sys
import etl
from llm.predibase_sentiment import *

def test_etl(data: dict) -> None:
    """Tests the ETL Pipeline."""

    API_TOKEN = 'pb_2lVSWVmcVQGkFuKPuQDvIQ'
    database = 'app/dashboard/databases/feedback.db'

    predibase = PredibaseSentiment(API_TOKEN, 'review-sentiment-model/3')
    etl.etl(data, database, predibase)

    return "Success!"

if __name__ == '__main__':

    feedback = [('The tour group was slighty disrespectful.', 'Miscellaneous'), 
                ('The tour guide started picking up litter. A little better than before.', 'Environment'),
                ('It seems the tour guide has better briefed the tourists on their environmental impacts.', 'Environment'), 
                ('The tour guide did a better job in telling the tourists to respect our culture.', 'Culture'),
                ('The tour company has started to give us incentives. A better change than before.', 'Miscellaneous')
                ]
    
    for index, f in enumerate(feedback):
        data = {
        'id': index,
        'community': 'Haenyeo',
        'category': f[1],
        'time': datetime.datetime.now(),
        'feedback': f[0]
    }

        test = test_etl(data)
        print(test)