import mysql.connector
from Models.SessionObject import SessionObject

class ConnectionDB:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost",user="root",password="password",database="POOTarea2")

    def RegistrarSesion(self, object : SessionObject):
        try:
            mycursor = self.connection.cursor()
            sql = """INSERT INTO Sessions (Username,Password,Firstname,
            Lastname,Currency,GamesPlayed,GamesLost,GamesWon,AvailableBalance) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
            val = (object.GetUsername(),object.GetPassword(),object.GetFirstname(),object.GetLastname(),object.GetCurrency(),
                    object.GetGamesPlayed(), object.GetGamesLost(),object.GetGamesWon(),object.GetAvailableBalance())

            mycursor.execute(sql, val)
            self.connection.commit()
            return True
        except:
            return False

    def GuardarSesion(self, object : SessionObject):
        try:
            mycursor = self.connection.cursor()
            sql = """UPDATE Sessions SET Username = %s,Password=%s,Firstname=%s, 
            Lastname=%s,Currency=%s,GamesPlayed=%s,GamesLost=%s,GamesWon=%s,AvailableBalance=%s 
            WHERE SessionId=%s;"""
            val = (object.GetUsername(),object.GetPassword(),object.GetFirstname(),object.GetLastname(),object.GetCurrency(),
                    object.GetGamesPlayed(), object.GetGamesLost(),object.GetGamesWon(),object.GetAvailableBalance(),
                    object.GetSessionId())

            mycursor.execute(sql, val)
            self.connection.commit()
            return True
        except:
            return False
        
    def VerificarSesion(self, username):
        try:
            ret = False
            mycursor = self.connection.cursor()
            sql = "SELECT * FROM Sessions WHERE username = %s;"
            val =(username,)
            mycursor.execute(sql,val)
            myresult = mycursor.fetchall()

            for x in myresult:
                ret = True
                break
            
            return ret
        except:
            return False

    def ObtenerSesion(self, username) -> SessionObject:
        try:
            ret = SessionObject()
            mycursor = self.connection.cursor()
            sql = "SELECT * FROM Sessions WHERE username = %s;"
            val =(username,)
            mycursor.execute(sql,val)
            myresult = mycursor.fetchall()

            for x in myresult:
                ret.SetSessionId(int(x[0]))
                ret.SetUsername(str(x[1]))
                ret.SetPassword(str(x[2]))
                ret.SetFirstname(str(x[3]))
                ret.SetLastname(str(x[4]))
                ret.SetCurrency(str(x[5]))
                ret.SetGamesPlayed(int(x[6]))
                ret.SetGamesLost(int(x[7]))
                ret.SetGamesWon(int(x[8]))
                ret.SetAvailableBalance(float(x[9]))
                break
            
            return ret
        except:
            return SessionObject()
