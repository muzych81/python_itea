"""
    Обновите генератор паролей из hw5/password_gen.py таким образом, чтобы:
    1. Все сгенерированные пароли записывались в файл passwords.txt
    2. После генерации пароля, сравнить его с содержимым файла.
        Если в файле уже записан такой пароль,
        то вывести сообщение с предупреждением "Insecure password".
    3*. Программа должна генерировать только уникальные пароли.
        Если в результате пункта 2 пароль уже содержится в файле, то генерируем
        его заново.
    * дополнительно стоит обрабатывать количество попыток генерации,
    так как после того, как будут сгенерированы все возможные комбинации,
    программа зациклится либо уйдет в бесконечную рекурсию и сломается
"""
from random import choice, randint
from string import ascii_lowercase, ascii_letters, digits, punctuation, ascii_uppercase
from pathlib import Path


def main():
    BASE_DIR = Path(__file__).resolve().parent
    file_path = BASE_DIR / "files" / "password.txt"
    difficult = input("Введите сложность пароля 1,2,3 ")
    password = password_gen(difficult)
    print(password)
    file = open(file_path, "r")
    all_str = file.read()
    if all_str.count(password) > 0:
        print("Insecure password")
    file.close()
    file = open(file_path, "a")
    file.write(password + "\n")
    file.close()


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
