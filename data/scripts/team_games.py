import csv

import database
import oracles_headers

from pymongo import MongoClient

cols = oracles_headers.oracles_columns

def get_teams(filename):
    teams = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row[cols['Position']] == 'team'):
                team = row[cols['Team']]
                if (team not in teams):
                    teams[team] = [reader.line_num]
                else:
                    teams[team].append(reader.line_num)
    return teams

def get_team_games(filename):
    teams = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row[cols['Position']] == 'team'):
                gameid = row[cols['GameId']]
                team = row[cols['Team']]
                side = row[cols['Side']]
                result = row[cols['Result']]
                gamelength = row[cols['GameLength']]
                kills = row[cols['Kills']]
                deaths = row[cols['Deaths']]
                assists = row[cols['Assists']]
                game = {
                    "gameId": gameid,
                    "team": team,
                    "side": side,
                    "result": False if result == "0" else True,
                    "gamelength": int(gamelength),
                    "kills": int(kills),
                    "deaths": int(deaths),
                    "assists": int(assists)
                }

                if (team != None and team not in teams):
                    teams[team] = [game]
                else:
                    teams[team].append(game)
    
    return teams

def insert_team_games(db, filename):
    teamgames = get_team_games(filename)
    for team in teamgames.keys():
        for game in teamgames[team]:
            db.TeamGames.insert_one(game)

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
    for event in events:
        insert_team_games(db, f"{eventpath}/{event}.csv")
        print("...Game insertion complete")