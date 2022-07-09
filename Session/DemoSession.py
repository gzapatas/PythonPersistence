from datetime import datetime
import random
from Models.SessionObject import SessionObject
from Session.Session import Session
from Utils.Logger import Logger

class DemoSession(Session):
    def Register(self, sessionObject: SessionObject):
        pass
      
    def InitializeSession(self, username = "", password = ""):
        self.Logger.Information("Sesion demo iniciada","Game")
        self.SessionObject.SetAvailableBalance(1000.00)
        self.SessionObject.SetUsername("DemoClient")
        self.SessionObject.SetCurrency("VC")
        self.SessionObject.SetFirstname("Demo")
        self.SessionObject.SetLastname("Client")
        self.SessionObject.SetGamesPlayed(0)
        self.SessionObject.SetGamesWon(0)
        self.SessionObject.SetGamesLost(0)
        self.SessionObject.SetStarted(datetime.now())
        self.SessionObject.SetPassword("")

        return True
    
    def GetAvailableBalance(self):
        return self.SessionObject.GetAvailableBalance()

    def PlayGame(self):
        player = random.randint(1,13)
        house = random.randint(1,13)

        balance = self.SessionObject.GetAvailableBalance() - 1
        
        if balance < 0: 
            return False

        self.SessionObject.SetAvailableBalance(balance)
        self.SessionObject.SetGamesPlayed(self.SessionObject.GetGamesPlayed() + 1)

        if player > house: 
            self.Logger.Information("JUGADOR gana " + str(player) + " > " + str(house), "Juego")
            self.SessionObject.SetAvailableBalance(balance + 3)
            self.SessionObject.SetGamesWon(self.SessionObject.GetGamesWon() + 1)
        elif player < house:
            self.SessionObject.SetGamesLost(self.SessionObject.GetGamesLost() + 1)
            self.Logger.Information("CASA gana " + str(house) + " > " + str(player), "Juego")
        else:
            self.SessionObject.SetAvailableBalance(balance + 1)
            self.Logger.Information("Empate " + str(house) + " = " + str(player), "Juego")

        return True

