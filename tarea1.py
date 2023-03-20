from fc_aleatorio import print_alternating
import fc_trigoylog
print(f"1). Para ejecutar la funcion que imprima 10 numeros desde 100 a 120, en consecutivo par e impar y saltando los numeros 110,115 y 119","\n","2).Para calcular funciones trigonometricas y logaritmo natural")
opc=int(input("¿Cual funcion quiere ejecutar?: "))
if opc==1:
    if __name__ == '__main__':
        print_alternating()
elif opc==2:
    if __name__ == '__main__':
        x= int(input("Ingrese un número: "))
        resultado = fc_trigoylog.Funciones(x)
        print(resultado)
else:
    print(f"Error de digitacion")