from Menu.Menu import Menu
from Session.SessionFactory import SessionFactory
from Utils.Logger import Logger


class PlayReal(Menu):
    def Ejecutar(self):
        logger = Logger()
        session = SessionFactory.GetSession("Real")
        username = str(input('Ingrese su usuario: '))
        password = str(input('Ingrese su contraseña: '))
        status = session.InitializeSession(username,password)

        if not status:
            return

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