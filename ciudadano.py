class Citizen:
    def __init__(self, name: str, age: int, id: int):
        self.__name = name
        self.__age = age
        self.__id = id
    
    def getName(self) -> str:
        return self.__name
    
    def getAge(self) -> int:
        return self.__age
    
    def getId(self) -> int:
        return self.__id
    
    def setName(self, name: str):
        self.__name = name
        
    def setAge(self, age: int):
        if age >= 18:
            self.__age = age
        else:
            print("The citizen is not yet of legal age.")
            
    def setId(self, id: int):
        idstr = str(id)
        if len(idstr) >= 8 and len(idstr) <= 10:
            self.__id = id
        else:
            print("The ID must be between 8 and 10 digits.")
            
    def isAdult(self) -> bool:
        return self.__age >= 18
    
    def show(self):
        print(f"Name: {self.__name} - Age: {self.__age} - ID: {self.__id}")
        
def main():
    citizen = Citizen("Nicolás", 28, 1289384734)
    citizen.show()
    
if __name__ == "__main__":
    main()