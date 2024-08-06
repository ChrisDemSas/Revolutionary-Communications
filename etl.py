import pandas as pd
import datetime
import sqlite3
from llm.predibase_sentiment import PredibaseSentiment

def transform(data: dict, analyzer: PredibaseSentiment) -> pd.DataFrame:
    """Take in piece of data and an analyzer and process the data.
    
    
    """