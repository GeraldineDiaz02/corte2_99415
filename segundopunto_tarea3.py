def k(n, p):
    def calc_term(i):
        return i * p

    result = 0
    i = 1
    while i <= n:
        result += calc_term(i)
        i += 1
    return result