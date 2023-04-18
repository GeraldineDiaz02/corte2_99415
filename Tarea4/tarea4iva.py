def calcularIva(producto, valor_neto):
    with open("Alimentos.txt", "r") as f:
        contenido = [linea.strip().split(",") for linea in f.readlines()]

    for fila in contenido:
        if fila[1] == producto:
            nombre = fila[0]
            porcentajeIva = float(fila[2])
            valorBase = valor_neto / (1 + porcentajeIva)
            valorIva = valorBase * porcentajeIva
            return (nombre, valorBase, valorIva)

    return None

if __name__ == "__main__":
    calcularIva()
