
class Persona:
    def __init__(self):
        self.nombre=None
        self.apellido=None
        self.edad=None
        self.frase=None
    
    def hablar(self):
        return self.frase


def main():
    estudiante= Persona()
    estudiante.nombre="Jineth"
    estudiante.apellido="Diaz"
    estudiante.edad=21
    estudiante.frase="Soy muy chevere"

    futbolista= Persona()
    futbolista.nombre="Radamel"
    futbolista.apellido="Garcia"
    futbolista.edad=36
    futbolista.frase="Gooool"

    print(f"El estudiante dice: {estudiante.hablar()}")
    print(f"El señor futblista dice: {estudiante.hablar()}")

    print(id(estudiante), estudiante.nombre)#id del objeto
    print(id(futbolista),futbolista.nombre)#id del objeto
    futbolista=estudiante#cambiar el apuntador
    print(id(estudiante), estudiante.nombre)
    print(id(futbolista),futbolista.nombre)

if __name__== "__main__":

    main()