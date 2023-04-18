class Person:
    def __init__(self):
        self.name=None
        self.size=None
        self.weight=None

    def Index(self):
        IMC=self.weight/(self.size/100)**2
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
    
def main():
    student1=Person()
    student1.name="Pedro Caceres"
    student1.size=188
    student1.weight=97

    student2=Person()
    student2.name="María Perez"
    student2.size=160
    student2.weight=47

    student3=Person()
    student3.name="Julian Rodriguez"
    student3.size=158
    student3.weight=58

    student4=Person()
    student4.name="Jesica Fuentes"
    student4.size=170
    student4.weight=73

    me=Person()
    me.name="Jineth Diaz"
    me.size=170
    me.weight=64

    print(f"Student: {student1.name} your results are: {student1.Index()}")
    print(f"Student: {student2.name} your results are: {student2.Index()}")
    print(f"Student: {student3.name} your results are: {student3.Index()}")
    print(f"Student: {student4.name} your results are: {student4.Index()}") 
    print(f"Student: {me.name} your results are: {me.Index()}") 

    if __name__=="__main__":
        main()
    