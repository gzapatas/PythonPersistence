from datetime import datetime
from Menu.Menu import Menu
from Models.SessionObject import SessionObject
from Session.SessionFactory import SessionFactory


class Register(Menu):
    def Ejecutar(self):
        session = SessionFactory.GetSession("Real")
        so = SessionObject()
        
        print("")
        opcion = float(input('Ingrese el monto a cargar: '))
        so.SetAvailableBalance(opcion)
        opcion = str(input('Ingrese su usuario: '))
        so.SetUsername(opcion)
        opcion = str(input('Ingrese sus contraseña: '))
        so.SetPassword(opcion)
        opcion = str(input('Ingrese sus nombres: '))
        so.SetFirstname(opcion)
        opcion = str(input('Ingrese sus apellidos: '))
        so.SetLastname(opcion)

        so.SetCurrency("PEN")
        so.SetGamesPlayed(0)
        so.SetGamesWon(0)
        so.SetGamesLost(0)
        
        session.Register(so)