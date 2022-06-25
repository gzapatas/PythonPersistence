from Models.SessionObject import SessionObject
from Utils.Logger import Logger

class Session:
    def __init__(self):
        self.SessionObject = SessionObject()
        self.Logger = Logger()

    def Register(self, sessionObject: SessionObject):
        pass

    def InitializeSession(self, username = "", password = ""):
        pass

    def GetAvailableBalance(self):
        pass
    
    def PlayGame(self):
        pass


