from classes import oracles_headers

class PlayerRow:
    COLUMNS = oracles_headers.oracles_columns

    def __init__(self, row):
        self.ROW = row

    def GetCell(self, name):
        return self.ROW[self.COLUMNS[name]]

    def GetDatabaseObject(self):
        game = {
            "gameId": self.GameId(),
            "isComplete": self.IsComplete(),
            "league": self.League(),
            "year": self.Year(),
            "split": self.Split(),
            "date": self.Date(),
            "patch": self.Patch(),
            "side": self.Side(),
            "position": self.Position(),
            "player": self.Player(),
            "team": self.Team(),
            "champion": self.Champion(),
            "gameLength": self.GameLength(),
            "result": self.Result(),
            "kills": self.Kills(),
            "deaths": self.Deaths(),
            "assists": self.Assists()
        }
        return game


    def GameId(self):
        return self.GetCell('GameId')

    def IsComplete(self):
        return self.GetCell('IsComplete')

    def League(self):
        return self.GetCell('League')
    
    def Year(self):
        return self.GetCell('Year')

    def Split(self):
        return self.GetCell('Split')

    def Date(self):
        return self.GetCell('Date')

    def Patch(self):
        return self.GetCell('Patch')

    def Side(self):
        return self.GetCell('Side')

    def Position(self):
        return self.GetCell('Position')

    def Player(self):
        return self.GetCell('Player')

    def Team(self):
        return self.GetCell('Team')

    def Champion(self):
        return self.GetCell('Champion')

    def GameLength(self):
        return int(self.GetCell('GameLength'))
    
    def Result(self):
        return False if self.GetCell('Result') == "0" else True

    def Kills(self):
        return int(self.GetCell('Kills'))

    def Deaths(self):
        return int(self.GetCell('Deaths'))

    def Assists(self):
        return int(self.GetCell('Assists'))