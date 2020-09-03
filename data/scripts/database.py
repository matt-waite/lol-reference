import os
from pymongo import MongoClient

def create_db():
    if not os.path.isdir("/data/db"):
        os.mkdir("/data")
        os.mkdir("/data/db")


def connect_db():
    client = MongoClient()
    return client["game-data"]

if __name__ == "__main__":
    create_db()
    db = connect_db()
    print(db.list_collection_names())