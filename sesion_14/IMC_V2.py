#Programa con Setters y Getters


class Person:
    def __init__(self):
        self.__name=None
        self.__size=None
        self.__weight=None



    #----------Getters---------obtener valores, caracteristicas

    def getName(self):
        return self.__name
    def getSize(self):   
        return self.__size
    def getWeight(self):
        return self.__weight
    #----------Setters--------- modificar valores
    def setName(self,name:str):
        self.__name=name
    def setSize(self,size:int):
        self.__size=size
    def setWeight(self,weight:float):
        self.__weight=weight



#----------Metodo IMC -----

    def __Index(self):
        IMC=self.__weight/(self.__size/100)**2
        if IMC<18.5:
            return str("Low weight")
        elif IMC<=24.9:
             return str("Good weight")
        elif IMC<=29.9:
             return str("Overweight")
        elif IMC<=34.9:
             return str("Obesity 1")
        elif IMC<=39.9:
             return str("Obesity 2")
        else:
            return str("Morvid obesity")
    
    def getIMC(self):
         return self.__Index()
    
def main():
        entrance=[]
        for i in range(3):
             entrance.append(input("Entrance"))

        me=Person()
        me.setName(entrance[0])
        me.setSize(int(entrance[1]))
        me.setWeight(float(entrance[2]))
        
        print(f"Person: {me.getName()} your result are:{me.getIMC()}")

       
    

if __name__=="__main__":
        main()
    