string = "Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry."

# 1. Удалить из строки символы ','.
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'

string = string.replace(',','')
print('1',string)

# 2. Найти индекс самой последней буквы 'i' в строке.
#    Результат: 54

print('2',string.rfind('i'))

# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6

print('3',string.lower().count('i'))

# 4. Найти и вывести срез строки от 3 буквы 's' до 6 пробела.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов, вторым
#     параметром можно передать индекс, от которого делать поиск find('s', 12))

pos_s = 0
for i in range(3):
    pos_s = string.find('s',pos_s+1)
pos_space = 0
for i in range(6):
    pos_space = string.find(' ',pos_space+1)
print('4',string[pos_s:pos_space])

# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'

half = len(string) // 2
print('5',string[0:half] * 3 + string[half:len(string)])