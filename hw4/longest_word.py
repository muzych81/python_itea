"""
    1. Вводится строка
    2. Программа считает количество слов в введенной строке и выводит на экран.
    2. Программа определяет самое длинное слово и его длину и выводит на экран.
    ___________________________________________________________________________
    Например:
    >>> Hello,world! I am learning python.
    Слов в введенной строке: 6
    Самое длинное слово: "learning" (8 символов)
"""

import string

strin = input("Enter a string:")
pure_string = ''
longest_word =''
word_count = 0
for i in strin:
    if i in string.ascii_letters:
        pure_string = pure_string + i
    else:
        pure_string = pure_string + ' '
words = (pure_string.split())

for word in words:
    word_count +=1
    if len(word) > len(longest_word):
        longest_word = word
print(f'Count of the words:{word_count}, longest_word:{longest_word}, longest word count:{len(longest_word)}')
