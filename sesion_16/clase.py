class Citizen():
    def __init__(self) :
        self.__name=None
        self.__lenguage=None
    
    def getName(self):
        return self.__name
    def getLenguage(self):
        return self.__lenguage
    
    def setName(self, name:str):
        self.__name=name
    def setLenguage(self,lenguage:str):
        self.__lenguage=lenguage
#------------Sobrecarga---------------------
    def  greetings(self):
        return "Quoi de beau!"
#-------------Sub class son-----------------       
class Colombia(Citizen):
    def __init__(self):
        super().__init__()
        self.__cc=None
    
    def getCc(self):
        return self.__cc
    def setCc(self,cc:int):
        self.__cc=cc

    def  greetings(self):
        return "Hola"
#----------------Subclass ------------------
class England(Citizen):
    def __init__(self):
        super().__init__()
        self.__id=None
    
    def getId(self):
        return self.__id
    def setId(self,id:int):
        self.__id=id

    def  greetings(self):
        return "Hello"
#----------------Subclass ------------------
class China(Citizen):
    def __init__(self):
        super().__init__()
        self.__shengfenzheng=None
    
    def getShengfenzheng(self):
        return self.__shengfenzheng
    def setShengfenzheng(self,shengfenzheng:int):
        self.__shengfenzheng=shengfenzheng

    def  greetings(self):
        return "NiGanMaYa!!"

def giveGreetings(obj):            #polimorfismos
    return obj.greetings()

def main():
    Colombian= Colombia()
    Colombian.setName("Kevin")
    Colombian.setLenguage("Spanish")
    Colombian.setCc(154862)

    English= England()
    English.setName("Richard")
    English.setLenguage("Englis")
    English.setId(8446548)

    Chinese =China()
    Chinese.setName("Liu")
    Chinese.setLenguage("Chinese")
    Chinese.setShengfenzheng (4798454)

    Citizen1= Citizen()
    Citizen1.setName ("Carla")
    Citizen1.setLenguage("French")
    
    print(f"\tName: {Citizen1.getName()}\n"+\
          f"\tLenguage: {Citizen1.getLenguage()}\n"+\
        f'\t'+giveGreetings(Citizen1)+"\n")

    print(f"\tName: {Colombian.getName()}\n"+\
          f"\tLenguage: {Colombian.getLenguage()}\n"+\
          f"\tDocument cc: {Colombian.getCc()}\n"+\
            f'\t'+giveGreetings(Colombian)+"\n")
    
    print(f"\tName: {English.getName()}\n"+\
          f"\tLenguage: {English.getLenguage()}\n"+\
          f"\tDocument id: {English.getId()}\n"+\
            f'\t'+giveGreetings(English)+"\n")
    
    print(f"\tName: {Chinese.getName()}\n"+\
          f"\tLenguage: {Chinese.getLenguage()}\n"+\
          f"\tDocument shengfenzheng: {Chinese.getShengfenzheng()}\n"+\
            f'\t'+giveGreetings(Chinese)+"\n")

if __name__=="__main__":
    main()