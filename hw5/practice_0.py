"""
    Напишите функцию, которая не принимает водных параметров,
    запрашивает у пользователя username, валидирует его и возвращает.
    Валидации:
    - мимимальное количество символов 6 (len)
    - максимальное количество симолов 20 (len)
    - доступны только латинские буквы в нижнем регистре и _ (in, string lib)
    - username не может начинаться символом _ (.startswith())
    Если какое-то из требований не выполняется, запрашиваем повторный ввод.
    * смотрите lesson5/_6_practice_valid.py
"""
import string


def main():
    username = get_username()
    print(f"Добро пожаловать, {username}!")


def get_username() -> str:
    name = input('Enter username ')
    allowed_symbols = string.ascii_lowercase + '_'
    valid = True
    for c in name:
        if c not in allowed_symbols:
            valid = False
    if (len(name) < 6) or (len(name) > 20) or name.startswith('_') or valid == False:
        return get_username()
    return name


if __name__ == "__main__":
    main()
