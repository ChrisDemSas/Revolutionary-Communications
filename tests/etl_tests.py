import pandas as pd
import sqlite3
import filepaths as fp
import sys
sys.path.append(fp.UTILS_FILEPATH)
import predibase as pb
import datetime

def test_predibase() -> pd.DataFrame:
    """Tests a predibase instance to create a sentiment."""

    data = {
        'feedback': ['The tour group was very respectful to our culture.'],
        'time': [datetime.datetime.now()],
        'category': ['culture']
    }

    predibase = pb.PredibaseSentiment('pb_2lVSWVmcVQGkFuKPuQDvIQ', 
                          'review-sentiment-model/3')

    data = predibase.sentiment(data)

    return data

if __name__ == '__main__':
    data = test_predibase()

    print(data)