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

def get_player_games(file, name):
    games = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row[cols['Player']] == name):
                team = row[cols['Team']]
                position = row[cols['Position']]
                champion = row[cols['Champion']]
                result = row[cols['Result']]
                kills = row[cols['Kills']]
                deaths = row[cols['Deaths']]
                assists = row[cols['Assists']]
                games.append({
                    "player": name,
                    "team": team,
                    "position": position,
                    "champion": champion,
                    "result": False if result == "0" else True,
                    "kills": int(kills),
                    "deaths": int(deaths),
                    "assists": int(assists)
                })
    return games

if __name__ == "__main__":
    db = database.connect_db()
    event = "../event/EU_LCS_Summer_2014.csv"
    players = get_players(event)
    for player in players:
        games = get_player_games(event, player)
        wins = 0
        losses = 0
        for game in games:
            if game['result']:
                wins += 1
            else:
                losses += 1
        print(f"{player}: ({wins}-{losses})")