def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

if __name__ == "__main__":

    num = int(input("Ingrese un número: "))

    fact = factorial(num)

    print(f"El factorial de {num} es {fact}")