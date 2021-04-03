"""
    Модифицируйте форму регистрации из hw5/reg_form.py таким образом, чтобы:
    1. Все данные пользователей сохранялись в файл users.txt в любом формате.
    2. В файл errors.txt записывать все ошибочные либо не валидные вводы.
        (не валидный номер телефона, email и т.д.)
"""
from pathlib import Path


def main():
    BASE_DIR = Path(__file__).resolve().parent
    file_path_users = BASE_DIR / "files" / "users.txt"
    file_users = open(file_path_users, 'a')
    phone = get_phone()
    email = get_email()
    password = ''
    repassword = ' '
    while repassword != password:
        password = get_password()
        print("Повторите парль: ")
        repassword = get_password()
    print(f'Поздравляем с успешной регистрацией!\nВаш номер телефона {phone}\nВаш email {email}')
    print(f'Ваш пароль {"*" * len(password)}')

    print(f'phone={phone}, email={email}, password={password}', file=file_users)
    file_users.close()


def error_log(error: str):
    BASE_DIR = Path(__file__).resolve().parent
    file_path_errors = BASE_DIR / "files" / "errors.txt"
    file_errors = open(file_path_errors, 'a')
    print(error, file=file_errors)
    file_errors.close()


def get_phone():
    phone = input("Введите номер телефона: ")
    digits = '0123456789'
    digits_phone = ''
    for c in phone:
        if c in digits:
            digits_phone += c
    if len(digits_phone) < 9:
        error_log("phone error:" + digits_phone)
        return get_phone()
    else:
        phone = "380" + digits_phone[len(digits_phone) - 9:len(digits_phone)]
        return phone


def get_email():
    email = input("Введите e-mail: ")
    if len(email) > 6 and email.count('@') == 1:
        return email
    else:
        error_log("email error:" + email)
        return get_email()


def get_password():
    up = 0
    low = 0
    dig = 0
    sp = 0
    password = input("Введите пароль: ")
    for c in password:
        if c.isupper():
            up += 1
        if c.islower():
            low += 1
        if c.isdigit():
            dig += 1
        if c.isspace():
            sp += 1
    if up > 0 and low > 0 and dig > 0 and len(password) > 7 and sp == 0:
        return password
    else:
        error_log("password error:" + password)
        return get_password()


if __name__ == "__main__":
    main()
