def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

if __name__ == "__main__":
    # Pedimos al usuario que ingrese un número
    num = int(input("Ingrese un número: "))

    # Calculamos su factorial usando la función factorial
    fact = factorial(num)

    # Imprimimos el resultado
    print(f"El factorial de {num} es {fact}")