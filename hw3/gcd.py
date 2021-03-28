"""
    Алгоритм Евклида. НОД - наибольший общий делитель
    1. Большее число делим на меньшее.
    2. Если делится без остатка, то меньшее число и есть НОД (выходим из цикла)
    3. Если есть остаток, то большее число заменяем на остаток от деления.
    4. Переходим к 1 пункту.
"""
a = int(input("введите первое число: "))
b = int(input("введите второе число: "))
while True:
    if (a > b):
        if (a % b == 0):
            gcd = b
            break
        else:
            a = a % b
    elif (b > a):
        if (b % a == 0):
            gcd = a
            break
        else:
            b = b % a
    else:
        gcd = a
        break
print("НОД: ", gcd)
