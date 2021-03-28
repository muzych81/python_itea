"""
    Необходимо реализовать программу, которая принимает текст и удаляет из него
    все, что находится в скобочках "(", ")". Скобки могут быть вложенными.
    И выводит получившийся текст.
    ___________________________________________________________________________
    Например:
    >>> Программа принимает текст(вводится с клавиатуры(с помощью input())),
    форматирует его(удаляет все скобочки(и их содержимое)) и выводит на экран.
    Результат:
    Программа принимает текст, форматирует его и выводит на экран.
"""
strin = "Программа (классная) принимает текст(вводится с клавиатуры(с помощью input())) " + \
        "форматирует его(удаляет все скобочки(и их содержимое)) и выводит на экран " + \
         "Результат:"

cut = 0
result = ''
for i in strin:
    if i == '(':
        cut += 1
    if cut == 0:
        result += i
    if i == ')':
        cut -= 1
print(result)