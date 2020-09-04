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

def get_player_games(filename):
    players = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row[cols['Position']] != 'team'):
                player = row[cols['Player']]
                team = row[cols['Team']]
                position = row[cols['Position']]
                champion = row[cols['Champion']]
                result = row[cols['Result']]
                kills = row[cols['Kills']]
                deaths = row[cols['Deaths']]
                assists = row[cols['Assists']]
                game = {
                    "player": player,
                    "team": team,
                    "position": position,
                    "champion": champion,
                    "result": False if result == "0" else True,
                    "kills": int(kills),
                    "deaths": int(deaths),
                    "assists": int(assists)
                }

                if (player != None and player not in players):
                    players[player] = [game]
                else:
                    players[player].append(game)

    return players

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
        #"World_Championship_2014"
    ]
    for event in events:
        playergames = get_player_games(f"{eventpath}/{event}.csv")
        for player in playergames.keys():
            for game in playergames[player]:
                db.PlayerGames.insert_one(game)
        print("...Game insertion complete")
        