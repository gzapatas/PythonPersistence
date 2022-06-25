from Session.DemoSession import DemoSession
from Session.RealSession import RealSession

class SessionFactory:
    @staticmethod
    def GetSession(type):
        if type == "Demo":
            return DemoSession()
        else:
            return RealSession()
