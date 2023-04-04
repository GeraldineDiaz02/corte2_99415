def calcular_iva(producto, valor_neto):
    with open("Alimentos.txt", "r") as f:
        contenido = [linea.strip().split(",") for linea in f.readlines()]

    for fila in contenido:
        if fila[0] == producto:
            nombre = fila[1]
            porcentaje_iva = float(fila[2])
            valor_base = valor_neto / (1 + porcentaje_iva)
            valor_iva = valor_base * porcentaje_iva
            return (nombre, valor_base, valor_iva)

    return None

while True:
    producto = input("Ingrese el código del producto o escriba 'salir' para terminar: ")
    if producto == "salir":
        break

    valor_neto = float(input("Ingrese el valor neto del producto: "))
    resultado = calcular_iva(producto, valor_neto)

    if resultado is None:
        print("El código del producto no fue encontrado.")
    else:
        nombre, valor_base, valor_iva = resultado
        print("Producto: {}".format(nombre))
        print("Valor base: ${:,.2f}".format(valor_base))
        print("IVA ({:.0%}): ${:,.2f}".format(valor_iva / valor_base, valor_iva))
        print("Valor bruto: ${:,.2f}\n".format(valor_neto))
