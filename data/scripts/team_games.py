import csv

import database

from pymongo import MongoClient
from classes import oracles_headers

from classes import team_row
TeamRow = team_row.TeamRow

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
                teamgame = TeamRow(row)
                team = teamgame.Team()
                if (team != None and team not in teams):
                    teams[team] = [teamgame.GetDatabaseObject()]
                else:
                    teams[team].append(teamgame.GetDatabaseObject())
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

    '''
    teamgames = get_team_games("../event/EU_LCS_Spring_2014.csv")
    for team in teamgames.keys():
        for game in teamgames[team]:
            print(f"{team}: {game['kills']}/{game['deaths']}/{game['assists']}")
    '''

    for event in events:
        insert_team_games(db, f"{eventpath}/{event}.csv")
        print("...Game insertion complete")