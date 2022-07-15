
import random
from Menu.MenuFactory import MenuFactory
from Persistence.ConnectionDb import ConnectionDB

print("Bienvenido al juego carta mayor")
random.seed(-6789)

while True:
    print("")
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
