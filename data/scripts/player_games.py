import csv

import database

from pymongo import MongoClient
from classes import oracles_headers

from classes import player_row
PlayerRow = player_row.PlayerRow

cols = oracles_headers.oracles_columns

def get_players(filename):
    players = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row[cols['Position']] != 'team'):
                player = row[cols['Player']]
                if (player not in players):
                    players[player] = [reader.line_num]
                else:
                    players[player].append(reader.line_num)
    return players

def get_player_games(filename):
    players = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row[cols['Position']] != 'team'):
                playergame = PlayerRow(row)
                player = playergame.Player()
                if (player != None and player not in players):
                    players[player] = [playergame.GetDatabaseObject()]
                else:
                    players[player].append(playergame.GetDatabaseObject())
    return players

def insert_player_games(db, filename):
    playergames = get_player_games(filename)
    for player in playergames.keys():
        for game in playergames[player]:
            db.PlayerGames.insert_one(game)

if __name__ == "__main__":
    db = database.connect_db()
    eventpath = "../event"
    events = [
        "EU_CS_Spring_2014",
        "EU_CS_Spring_2014_Playoffs",
        "EU_LCS_Spring_2014",
        "EU_LCS_Spring_2014_Playoffs",
        "EU_CS_Summer_2014",
        "EU_CS_Summer_2014_Playoffs",
        "EU_LCS_Summer_2014",
        "EU_LCS_Summer_2014_Playoffs",
        "NA_CS_Spring_2014",
        "NA_LCS_Spring_2014",
        "NA_LCS_Spring_2014_Playoffs",
        "NA_CS_Summer_2014",
        "NA_LCS_Summer_2014",
        "NA_LCS_Summer_2014_Playoffs",
        "World_Championship_2014"
    ]

    '''
    playergames = get_player_games("../event/NA_LCS_Summer_2014.csv")
    for player in playergames.keys():
        kills = 0
        for game in playergames[player]:
            kills += game['kills']
        print(f"{player}: {kills}")
    '''

    for event in events:
        insert_player_games(db, f"{eventpath}/{event}.csv")
        print("...Game insertion complete")