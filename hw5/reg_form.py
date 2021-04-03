"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.
    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)
    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер
    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.
    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа
    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.
    Программа выводит сообщение:
    Поздравляем с успешной регистрацией!
    Ваш номер телефона: +380501234567
    Ваш email: example@mail.com
    Ваш пароль: ********** (кол-во  == кол-ву символов пароля)
"""


def main():
    phone = get_phone()
    email = get_email()
    password = ''
    repassword = ' '
    while repassword != password:
        password = get_password()
        print("Повторите парль: ")
        repassword = get_password()
    print(f'Поздравляем с успешной регистрацией!\nВаш номер телефона {phone}\nВаш email {email}')
    print(f'Ваш пароль {"*"*len(password)}')

def get_phone():
    phone = input("Введите номер телефона: ")
    digits = '0123456789'
    digits_phone = ''
    for c in phone:
        if c in digits:
            digits_phone += c
    if len(digits_phone) < 9:
        return get_phone()
    else:
        phone = "380" + digits_phone[len(digits_phone) - 9:len(digits_phone)]
        return phone


def get_email():
    email = input("Введите e-mail: ")
    if len(email) > 6 and email.count('@') == 1:
        return email
    else:
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
        return get_password()


if __name__ == "__main__":
    main()
