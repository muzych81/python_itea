"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.
    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)
    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))
    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "здесь_исходная_строка".
        Результат: "здесь_измененная_строка_после_выполненного_пункта".
    (Использовать форматирование строк f'{}')
"""
import string

# можно заменить данную строку на input()
#strin = "Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY."
strin = input("input string: ")

#1
up_count = 0
low_count = 0

for i in strin:
    if i in string.ascii_lowercase:
        low_count += 1
    if i in string.ascii_uppercase:
        up_count +=1
if low_count > up_count:
    result = strin.lower()
elif up_count > low_count:
    result = strin.upper()
else:
    result = strin.swapcase()
print(f'1. Исходная строка: {strin}\nРезультат: {result}')

#2
pure_string = ''
for i in strin:
    if i in string.ascii_letters:
        pure_string = pure_string + i
    else:
        pure_string = pure_string + ' '
words = (pure_string.split())

capital = True

for word in words:
    if word[0].islower():
        capital = False

if capital:
    result = 'done. ' + strin
else:
    result = 'draft: ' + strin[5:]
print(f'2. Исходная строка: {strin}\nРезультат: {result}')

#3
if len(strin) > 20:
    result = strin[:20]
else:
    result = strin.ljust(20,'@')
print(f'3. Исходная строка: {strin}\nРезультат: {result}')