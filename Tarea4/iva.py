from tarea4iva import calcularIva

while True:
        producto = input("Ingrese el nombre del producto o escriba 'salir' para terminar: ")
        if producto == "salir":
            break

        valorNeto = float(input("Ingrese el valor neto del producto: "))
        resultado = calcularIva(producto, valorNeto)

        if resultado is None:
            print("El código del producto no fue encontrado.")
        else:
            nombre, valorBase, valorIva = resultado
            print("Producto: {}".format(nombre))
            print("Valor base: ${:,.2f}".format(valorBase))
            print("IVA ({:.0%}): ${:,.2f}".format(valorIva / valorBase, valorIva))
            print("Valor neto: ${:,.2f}\n".format(valorNeto))
