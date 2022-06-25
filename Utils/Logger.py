from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Logger():
    _instance = None

    def __new__(cls):
        if Logger._instance is None:
            Logger._instance = object.__new__(cls)
            Logger._name = 'Logger'
        return Logger._instance
    
    def Warning(self,message,key):
        print(bcolors.WARNING + "[" + key + "]" + bcolors.ENDC + " - " + message + " - " + datetime.now().isoformat())
    
    def Information(self,message,key):
        print(bcolors.OKBLUE + "[" + key + "]" + bcolors.ENDC + " - " + message + " - " + datetime.now().isoformat())
    
    def Error(self,message,key):
        print(bcolors.FAIL + "[" + key + "]" + bcolors.ENDC + " - " + message + " - " + datetime.now().isoformat())
    
    def Debug(self,message,key):
        print(bcolors.OKGREEN + "[" + key + "]" + bcolors.ENDC + " - " + message + " - " + datetime.now().isoformat())
    

