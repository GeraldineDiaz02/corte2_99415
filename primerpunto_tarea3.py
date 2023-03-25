import random as r

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(r.randint(0, 100))
        matriz.append(fila)
    return matriz

def encontrar_max_min(matriz):
    maximo = matriz[0][0]
    minimo = matriz[0][0]
    max_fila = 0
    max_columna = 0
    min_fila = 0
    min_columna = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
                max_fila = i
                max_columna = j
            if matriz[i][j] < minimo:
                minimo = matriz[i][j]
                min_fila = i
                min_columna = j
    return (maximo, minimo, max_fila, max_columna, min_fila, min_columna)

def ordenar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    lista_numeros = []
    for i in range(filas):
        for j in range(columnas):
            lista_numeros.append(matriz[i][j])
    lista_numeros.sort(reverse=True)
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = lista_numeros.pop(0)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

def mimatriz():
    matriz = crear_matriz(5, 10)
    print("Matriz generada:")
    imprimir_matriz(matriz)
    maximo, minimo, max_fila, max_columna, min_fila, min_columna = encontrar_max_min(matriz)
    print(f"El número más alto es {maximo} en la posición ({max_fila}, {max_columna})")
    print(f"El número más bajo es {minimo} en la posición ({min_fila}, {min_columna})")
    matriz_ordenada = ordenar_matriz(matriz)
    print("Matriz ordenada:")
    imprimir_matriz(matriz_ordenada)

if __name__ == "__main__":
    mimatriz()