"""
    Нарисовать границу из * в списке.
    Количество элементов каждой строки уравнять по самой длинной в списке,
    центрировать текст и недостающие символы заполнить пробелами.
    [in]    ['python',
             'django']
    [out]   ['********',
             '*python*',
             '*django*',
             '********']
    [in]    ['py',
             'python']
    [out]   ['********',
             '*  py  *',
             '*python*',
             '********']
    Покрыть несколькими тестами.
"""


def main():
    in_ = ['python', 'django']

    out_ = ['********',
            '*python*',
            '*django*',
            '********']

    assert draw_border(in_) == out_
    in_ = ['py',
           'python']
    out_ = ['********',
            '*  py  *',
            '*python*',
            '********']

    assert draw_border(in_) == out_
    print("All tests passed successfully!")


def draw_border(input_list: list) -> list:
    max_len = 0
    for list_element in input_list:
        if len(list_element) > max_len:
            max_len = len(list_element)
    new_list = list()
    new_list.append("*" * (max_len + 2))
    for list_element in input_list:
        new_list.append("*" + list_element.center(max_len) + "*")
    new_list.append("*" * (max_len + 2))
    return new_list


if __name__ == "__main__":
    main()
