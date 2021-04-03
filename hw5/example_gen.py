"""
    Пример использования модулей random и string
    Программа выводит случайный спец-символ либо число.
    * можно делать выборку в цикле и конкатенировать все в одну строку,
    если нужно больше, чем 1 символ
"""

from random import choice
from string import digits, punctuation


def main():
    print(random_char(20))


def random_char(i):
    # генерируем строку для выборки
    tmp = digits + punctuation
    strin = ''
    for _ in range(i):
        # выбираем случайный символ из строки
        strin += choice(tmp)
    return strin


if __name__ == "__main__":
    main()
