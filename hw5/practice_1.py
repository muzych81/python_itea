"""
    Программу принимает на ввод строку string и число n.
    Выводит на экран строку с смещенными символами на число n.
    Весь код можно написать в одной функции main,
    но рекомендуется разбить код на несколько функций, например:
    - main
    - функция для получения не пустой строки.
    - функция для получения сдвига (целое число).
    - функция, которая делает сдвиг строки.
    Пример:
    Введите строку: python hello world
    Введите сдвиг: 5
    Результат: n hello worldpytho
    Введите строку: python hello world
    Введите сдвиг: -2
    Результат: ldpython hello wor
    * используйте индексы, срезы и возможно циклы
"""


def main():
    print(shift(input_string(), input_shift()))


def shift(string_, shift):
    return string_[shift:] + string_[:shift]


def input_shift():
    shift = input("Enter shift ")
    try:
        return int(shift)
    except ValueError:
        return input_shift()

def input_string():
    string_ = input("Enter not empty string: ")
    if len(string_) > 0:
        return string_
    else:
        return input_string()


if __name__ == "__main__":
    main()
