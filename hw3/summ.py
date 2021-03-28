"""
    Пользователь вводит начало и конец числового ряда.
    Если начало не введено - считать, что это 0.
    1. Программа считает и выводит на экран сумму числового ряда.
    2. Произведение нечетных чисел числового ряда.
    * обработать возможные ошибки
"""
try:
    begin = input("введите начало числового ряда ")
    if begin == "":
        begin = 0
    else:
        begin = int(begin)
    end = int(input("введите конец числового ряда "))
except ValueError:
    print("Введено не число")
else:
    summ = 0
    mulodd = 1
    for i in range(begin, end + 1):
        summ += i
        if i % 2 != 0:
            mulodd *= i

    print("summ", summ, "mulodd", mulodd)
