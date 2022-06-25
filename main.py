
from datetime import datetime
import random
from Menu.MenuFactory import MenuFactory
from Models.SessionObject import SessionObject
from Session.SessionFactory import SessionFactory

print("Bienvenido al juego carta mayor")
random.seed(-6789)

while True:
    print("")
    print("Que desea realizar")
    print(" 1) Jugar como invitado")
    print(" 2) Jugar como jugador")
    print(" 3) Registrarse")
    print(" 4) Salir")
    opcion = int(input('Opcion: '))
    menu = MenuFactory.ObtenerMenu(opcion)
    
    if menu is not None:
        menu.Ejecutar()