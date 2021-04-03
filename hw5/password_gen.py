"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)
    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)
    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""  # noqa: E501

from random import choice, randint
from string import ascii_lowercase, ascii_letters, digits, punctuation, ascii_uppercase


def main():
    difficult = input("Введите сложность пароля 1,2,3 ")
    print(password_gen(difficult))


def password_gen(difficult):
    if difficult == '1':
        strin = ''
        for _ in range(8):
            strin += choice(ascii_lowercase)
        return strin
    elif difficult == '2':
        strin = ''
        for _ in range(8):
            strin += choice(ascii_letters + digits)
        return strin
    elif difficult == '3':
        cap = 0
        low = 0
        dig = 0
        spec = 0
        while cap == 0 or low == 0 or dig == 0 or spec == 0:
            cap = 0
            low = 0
            dig = 0
            spec = 0
            strin = ''
            for _ in range(randint(8, 16)):
                cho = choice(digits + ascii_letters + punctuation)
                if cho in digits:
                    dig += 1
                if cho in punctuation:
                    spec += 1
                if cho in ascii_uppercase:
                    cap += 1
                if cho in ascii_lowercase:
                    low += 1
                strin += cho
        return strin


if __name__ == "__main__":
    main()
