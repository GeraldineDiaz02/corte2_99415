def k(n, p):
    result = 0
    i = 1
    while i <= n:
        result += i*p
        i += 1
    return result