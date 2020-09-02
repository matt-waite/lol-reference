import csv
import oracles_headers
import os
from pymongo import MongoClient

cols = oracles_headers.oracles_columns

def output_headers(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            print("columns = {")
            for entry in row:
                print(f"    '{entry}',")
            print("}")
            break

def getCell(row, col):
    return row[cols[col]]

def createDB():
    if not os.path.isdir("/data/db"):
        os.mkdir("/data")
        os.mkdir("/data/db")

def connectDB():
    client = MongoClient()
    return client["game-data"]

if __name__ == "__main__":
    #output_headers('../raw/2014_OraclesElixir.csv')
    createDB()
    db = connectDB()
    print(db.list_collection_names())

    match_totals = {}
    with open('../raw/2014_OraclesElixir.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            event_key = f"{getCell(row, 'League')} {getCell(row, 'Year')} {getCell(row, 'Split')}"
            if (getCell(row, 'PlayerId') == "100" or getCell(row, 'PlayerId') == "200"):
                if (event_key not in match_totals):
                    match_totals[event_key] = [row.values()]
                else:
                    match_totals[event_key].append(row.values())
    print(", ".join(match_totals["EU LCS 2014 Summer"][1]))