import random as r

def crear_lista():
    lista = []
    for i in range(10):
        lista.append(r.randint(1, 50))
    return lista

def mayor(lista):
    mayor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    print("El número mayor de la lista es:", mayor)

def primos(lista):
    primos = []
    for num in lista:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primos.append(num)
    print("Los números primos de la lista son:", primos)