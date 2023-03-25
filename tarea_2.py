from primer_punto import consultar_horario
from segundo_punto import crear_lista, mayor, primos
print(f"ALgoritmo que imprime horario desde materia","\n","Algoritmo que de una lita aleatoria clasifica sus numeros con el mayor y primos")

opc=int(input("Escoga una opcion del menu: "))

if opc==1:
    if __name__ == "__main__":
        materia = input("Ingrese la materia que desea consultar: ")
        consultar_horario(materia)

if opc==2:        
    if __name__ == "__main__":
        
        lista_aleatoria = crear_lista()

        print("Lista de números aleatorios:", lista_aleatoria)

        mayor(lista_aleatoria)

        primos(lista_aleatoria)