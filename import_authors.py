import json
import pandas as pd
import sys
from app import app
from database.db import db


# TODO Change this to use csv.DictReader instead of Pandas.read_csv
# See https://medium.com/casual-inference/the-most-time-efficient-ways-to-import-csv-data-in-python-cc159b44063d
def read_data(csv_file):
    return pd.read_csv(csv_file)


def import_authors(csv_file):
    ''' Delete db collection named 'authors'
        and create a new with the data of `csv_file`'''
    database = db.get_db()
    collection_name = 'author'
    db_authors = database[collection_name]

    # Delete `db` collection with the `collection_name`'''
    database.drop_collection(collection_name)

    data = read_data(csv_file)
    data_json = json.loads(data.to_json(orient='records'))
    db_authors.insert_many(data_json)


if __name__ == "__main__":
    import_authors(sys.argv[1])
