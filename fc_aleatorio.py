import random as r

def Aleatorio():
    num = r.randint(100, 120)
    while num in [110, 115, 119]:
        num = r.randint(100, 120)
    return num

def print_alternating():
    nums = []
    i = 0
    while len(nums) < 10:
        num = Aleatorio()
        if i % 2 == 0 and num % 2 == 0:
            nums.append(num)
            i += 1
        elif i % 2 != 0 and num % 2 != 0:
            nums.append(num)
            i += 1

    print(*nums)
if __name__ == '__main__':
    numeros = Aleatorio()
    print_alternating()

