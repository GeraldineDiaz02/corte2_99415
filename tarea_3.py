from primerpunto_tarea3 import mimatriz
from segundopunto_tarea3 import k
from tare3_terpunto import factorial

print(f"1). Matriz de 5x10 ordenada, numero mayor y menor", "\n","2). Funcion k(n,p)","\n","3). Funcion recursiva para calcular factorial")
opc=int(input("Escoja una opcion: "))

if opc ==1:
    mimatriz()

if opc==2:
    if __name__ == '__main__':
     n = int(input("Ingrese n: "))
    p = int(input("Ingrese p: "))
    resultado = k(n, p)
    print("El resultado es:", resultado)

if opc==3:
   if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    fact = factorial(num)
    print(f"El factorial de {num} es {fact}")
