
import os


class File:
    def Exists(self, filename):
        return os.path.exists(filename + ".json")
            
    def Save(self, filename, data):
        try:
            f = open(filename + ".json","w")
            f.write(data)
            f.flush()
            f.close()
        except :
            return False

        return True
    
    def Read(self, filename):
        try:
            f = open(filename + ".json", "r")
            data = f.read()
            f.close()

            return data
        except :
            return ""