"""
    Написать функцию, которая будет проверять счастливый билетик или нет.
    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
    Если количество цифр одной и второй половины не равно - билет не счастливый
"""


def main():
    assert is_lucky(1230) is True
    assert is_lucky(239017) is False
    assert is_lucky(134008) is True
    assert is_lucky(15) is False
    assert is_lucky(2020) is True
    assert is_lucky(199999) is False
    assert is_lucky(77) is True
    assert is_lucky(479974) is True
    assert is_lucky(4799731) is False
    assert is_lucky(1379974) is False

    print("All tests passed successfully!")


def is_lucky(ticket_num: int) -> bool:
    str_num = str(ticket_num)
    if len(str_num) % 2 != 0:
        return False
    first_half = 0
    second_half = 0
    half = int(len(str_num) / 2)
    for s in str_num[:half]:
        first_half += int(s)
    for s in str_num[half:]:
        second_half += int(s)
    if first_half == second_half:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
