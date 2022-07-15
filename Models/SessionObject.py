from datetime import datetime
import json
import dateutil.parser

class SessionObject:
    def __init__(self):
        self.SessionId = 0
        self.Username = ""
        self.Password = ""
        self.Firstname = ""
        self.Lastname = ""
        self.Currency = ""
        self.GamesPlayed = 0
        self.GamesLost = 0
        self.GamesWon = 0
        self.AvailableBalance = 0.00
    
    def SetSessionId(self, value):
        self.SessionId = value

    def GetSessionId(self):
        return self.SessionId

    def SetCurrency(self, value):
        self.Currency = value

    def GetCurrency(self):
        return self.Currency

    def SetUsername(self, value):
        self.Username = value

    def GetUsername(self):
        return self.Username
    
    def SetPassword(self, value):
        self.Password = value

    def GetPassword(self):
        return self.Password

    def SetFirstname(self, value):
        self.Firstname = value

    def GetFirstname(self):
        return self.Firstname

    def SetLastname(self, value):
        self.Lastname = value

    def GetLastname(self):
        return self.Lastname

    def SetGamesPlayed(self, value):
        self.GamesPlayed = value

    def GetGamesPlayed(self):
        return self.GamesPlayed

    def SetGamesLost(self, value):
        self.GamesLost = value

    def GetGamesLost(self):
        return self.GamesLost

    def SetGamesWon(self, value):
        self.GamesWon = value

    def GetGamesWon(self):
        return self.GamesWon

    def SetAvailableBalance(self, value):
        self.AvailableBalance = value

    def GetAvailableBalance(self):
        return self.AvailableBalance

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
    def fromJSON(self, info):
        if len(info) <= 0:
            return False

        obj = json.loads(info)

        self.SetUsername(obj["Username"])
        self.SetPassword(obj["Password"])
        self.SetFirstname(obj["Firstname"])
        self.SetLastname(obj["Lastname"])
        self.SetGamesPlayed(obj["GamesPlayed"])
        self.SetGamesLost(obj["GamesLost"])
        self.SetGamesWon(obj["GamesWon"])
        self.SetAvailableBalance(obj["AvailableBalance"])
        self.SetCurrency(obj["Currency"])

        return True




        
