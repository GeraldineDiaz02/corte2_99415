def factorial(n):
    def factorial_aux(n, acc):
        if n == 0:
            return acc
        else:
            return factorial_aux(n-1, n*acc)
        
    return factorial_aux(n, 1)

