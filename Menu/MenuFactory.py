import os
from Menu.PlayDemo import PlayDemo
from Menu.PlayReal import PlayReal
from Menu.Register import Register
from Utils.Logger import Logger

class MenuFactory:
    @staticmethod
    def ObtenerMenu(opcion: int):
        if opcion == 1:
            Logger().Information("Ud ha elegido jugar en modo demo", "Juego")
            return PlayDemo();
        elif opcion == 2:
            Logger().Information("Ud ha elegido jugar en modo real", "Juego")
            return PlayReal();
        elif opcion == 3:
            Logger().Information("Ud ha elegido registrarse", "Juego")
            return Register();
        elif opcion == 4:
            Logger().Warning("Ud ha finalizado el programa", "Juego")
            exit()
        else:
            return None