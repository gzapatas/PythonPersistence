import random
from Models.SessionObject import SessionObject
from Session.Session import Session
from Persistence.FilePersistence import File
from Persistence.ConnectionDb import ConnectionDB

class RealSession(Session):
    def Register(self, sessionObject: SessionObject):
        self.SessionObject = sessionObject
        db = ConnectionDB()

        if db.VerificarSesion(sessionObject.GetUsername()):
            self.Logger.Error("Ya existe una sesion de juego creada","Juego")
            return False

        if not db.RegistrarSesion(sessionObject):
            self.Logger.Error("No se pudo crear la sesion de juego","Juego")
            return False
        
        self.Logger.Information("Sesion de cliente registrada","Juego")

        return True
      
    def InitializeSession(self, username, password):
        db = ConnectionDB()

        self.SessionObject = db.ObtenerSesion(username)
        
        if self.SessionObject is None or self.SessionObject.GetSessionId() == 0:
            self.Logger.Error("No se encontro su sesion","Juego")
            return False

        if password != self.SessionObject.GetPassword():
            self.Logger.Error("Password incorrecto","Juego")
            return False
        
        self.Logger.Information("Sesion de cliente iniciada","Juego")

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
            self.SessionObject.SetGamesLost(self.SessionObject.GetGamesWon() + 1)
            self.Logger.Information("CASA gana " + str(house) + " > " + str(player), "Juego")
        else:
            self.SessionObject.SetAvailableBalance(balance + 1)
            self.Logger.Information("Empate " + str(house) + " = " + str(player), "Juego")

        db = ConnectionDB()
        if not db.GuardarSesion(self.SessionObject):
            self.Logger.Error("No guardar el resultado del juego","Juego")
            return False

        return True

        
