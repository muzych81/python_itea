"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) данные владельцев,
    чьи имена начинаются на букву "m" либо заканчиваются на "а"
    (регистр не имеет значения).
    В файл записывать данные в таком формате:
    1. +380501234561 - Имя
    2. +380501234562 - Имя
    3. +380501234563 - Имя
    4. +380501234564 - Имя
    ...
"""
from pathlib import Path
import re


def main():
    BASE_DIR = Path(__file__).resolve().parent
    file_path_in = BASE_DIR / "files" / "phone_book.txt"
    file_path_out = BASE_DIR / "files" / "edited_phone_book.txt"
    file_in = open(file_path_in, 'r')
    file_out = open(file_path_out, 'w')
    all_str = file_in.readlines()
    pos = 0
    for str_ in all_str:
        pos += 1
        result = re.search(r'(\b\w+\b)', str_).group().capitalize()
        print(f'{pos}. {get_phone(str_)} {result}', file=file_out)
    file_in.close()
    file_out.close()


def get_phone(str_: str):
    digits = '0123456789'
    digits_phone = ''
    for c in str_:
        if c in digits:
            digits_phone += c
    if len(digits_phone) < 9:
        return "invalid number"
    else:
        phone = "+380" + digits_phone[len(digits_phone) - 9:len(digits_phone)]
        return phone


if __name__ == "__main__":
    main()
