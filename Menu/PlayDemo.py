from Menu.Menu import Menu
from Session.SessionFactory import SessionFactory
from Utils.Logger import Logger


class PlayDemo(Menu):
    def Ejecutar(self):
        logger = Logger()
        session = SessionFactory.GetSession("Demo")
        session.InitializeSession()

        while True:
            print("")
            print("Que desea realizar")
            print(" 1) Jugar un juego")
            print(" 2) Volver al menu principal")
            
            opcion = int(input('Opcion: '))
            
            if opcion == 2:
                break

            logger.Debug("Creditos antes de jugar " + str(session.GetAvailableBalance()),"Juego")
            session.PlayGame()
            logger.Debug("Creditos despues de jugar " + str(session.GetAvailableBalance()),"Juego")