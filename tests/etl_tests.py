import pandas as pd
import sqlite3
import filepaths as fp
import sys
sys.path.append(fp.UTILS_FILEPATH)
from predibase import Predibase
import datetime

def test_predibase() -> None:
    """Tests a predibase instance to create a sentiment."""

    data = {
        'feedback': ['The tour group was very respectful to our culture.'],
        'time': [datetime.datetime.now()],
        'category': ['culture']
    }

    predibase = Predibase()