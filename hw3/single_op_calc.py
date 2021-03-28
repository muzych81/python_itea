""""
    Программа считает сумму/разницу/произведение/частное n чисел.
    Алгоритм:
    1. Пользователь вводит число n.
    2. Затем выбирает операцию (+, -, *, /).
    3. После этого вводит n чисел.
    4. Программа выводит результат и сообщение "Continue? (y/n)".
    5. Если пользователь вводит y, то программа выполняется сначала.
        Иначе - выводит сообщение 'Bye!' и прекращает свою работу.
"""

char = ""
while True:
    n = int(input("Enter number n "))
    op = input("Enter operation +, -, * , /")

    for i in range(n):
        print("Enter number ", i, end=" ")
        number = int(input())
        if (i == 0):
            if (op == "+"):
                result = 0
            elif (op == "-") or (op == "*") or (op == "/"):
                result = number
                continue

        if op == "+":
            result += number
        if op == "-":
            result -= number
        if op == "*":
            result *= number
        if op == "/":
            result /= number
    print("result ", result)
    ent = input("Continue? (Y/n)")
    if ent == "n":
        print("bye!")
        break
