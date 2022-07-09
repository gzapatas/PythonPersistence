from datetime import datetime
import json
import dateutil.parser

class SessionObject:
    def __init__(self):
        self.Username = ""
        self.Password = ""
        self.Firstname = ""
        self.Lastname = ""
        self.Currency = ""
        self.GamesPlayed = 0
        self.GamesLost = 0
        self.GamesWon = 0
        self.Started = datetime.now()
        self.AvailableBalance = 0.00
    
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
    
    def SetStarted(self, value: datetime):
        self.Started = value.isoformat()

    def GetStarted(self) -> datetime:
        return dateutil.parser.isoparse(self.Started)

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
        self.SetStarted(dateutil.parser.isoparse(obj["Started"]))
        self.SetAvailableBalance(obj["AvailableBalance"])
        self.SetCurrency(obj["Currency"])

        return True




        
