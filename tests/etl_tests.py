import pandas as pd
import sqlite3
import sys
import etl
from llm.predibase_sentiment import *
from datetime import timedelta
import random

def test_etl(data: dict) -> None:
    """Tests the ETL Pipeline."""

    API_TOKEN = ''
    database = 'app/databases/feedback.db'

    predibase = PredibaseSentiment(API_TOKEN, 'review-sentiment-model/3')
    etl.etl(data, database, predibase)

    return "Success!"

if __name__ == '__main__':

    feedback = pd.read_csv('dataset/initial.csv')

    data = feedback.to_dict("records")
    counter = 0

    for item in data:
        feedback = item['feedback']
        category = item['category']
        community = item['community ']
        r = random.randint(1, 60)

        todays_date = datetime.datetime.today().strftime('%Y-%m-%d')
        todays_date = datetime.datetime.strptime(todays_date, '%Y-%m-%d') - timedelta(days=r)

        data = {
        'id': counter,
        'community': community,
        'category': category,
        'time': todays_date,
        'feedback': feedback}

        test = test_etl(data)
        print(f"{counter}. {test}")

        counter += 1