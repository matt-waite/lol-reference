import oracles_headers
import csv
import os
from pymongo import MongoClient

cols = oracles_headers.oracles_columns

def createDB():
    if not os.path.isdir("/data/db"):
        os.mkdir("/data")
        os.mkdir("/data/db")


def connectDB():
    client = MongoClient()
    return client["game-data"]

if __name__ == "__main__":
    createDB()
    db = connectDB()
    print(db.list_collection_names())