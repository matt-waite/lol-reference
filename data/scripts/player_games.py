import csv

import database
import oracles_headers

from pymongo import MongoClient

cols = oracles_headers.oracles_columns

def get_player(row):
    position = row[cols['Position']]
    if (position != "team"):
        return row[cols['Player']]

def get_players(filename):
    players = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player = get_player(row)
            if (player != None):
                if (player not in players):
                    players[player] = [reader.line_num]
                else:
                    players[player].append(reader.line_num)
    return players

def get_player_games(name):
    return []

if __name__ == "__main__":
    db = database.connect_db()
    players = get_players("../event/EU_LCS_Summer_2014.csv")
    for player in players.keys():
        print(f"{player}: {len(players[player])}")