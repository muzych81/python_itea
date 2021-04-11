"""
    1. Сгенерировать список случайной длины заполнив его случайными числами
    (используйте random, диапазон чисел произвольный)
    2. Вывести на экран числа из списка в обратном порядке через пробел
    3. Извлечь первое число, возвести его в квадрат и вставить в средину списка
    4. Удалить из списка простые числа.
    5. Записать в файл list_info.txt строчки:
        - 1. элементы списка через запятую
        - 2. количество элементов списка
        - 3. самое маленькое число списка
        - 4. сумму чисел списка кратных 3
"""

import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main():
    list_ = generate_list()
    print("surce_list:", list_)
    print("reverse list: ", end="")
    reverse_list_print(list_)
    print("\nFirst in center list:", end="")
    print(first_in_center(list_))
    print("removed simple list", remove_simple(list_))

    file_path = BASE_DIR / "list_info.txt"
    with open(file_path, "a") as f:
        print("coma separated list:", coma_separated_list(list_), file=f)
        print("length:", len(list_), file=f)
        print("minimal:", min(list_), file=f)
        print("sum 3:", get_sum_3(list_), file=f)


def generate_list() -> list:
    new_list = list()
    for i in range(random.randint(1, 20)):
        new_list.append(random.randint(1, 100))
    return new_list


def reverse_list_print(list_: list) -> list:
    new_list = list_[::-1]
    for i in new_list:
        print(i, end=" ")


def first_in_center(list_: list) -> list:
    list_.insert(len(list_) // 2, int(list_[0]) ** 2)
    return list_


def is_simple(i: int) -> bool:
    for _ in range(2, i):
        if i % _ == 0:
            return False
    return True


def remove_simple(list_: list) -> list:
    new_list = list()
    for i in list_:
        if not is_simple(i):
            new_list.append(i)
    return new_list


def coma_separated_list(list_: list) -> str:
    string_ = ''
    for i in list_:
        string_ = string_ + str(i) + ','
    return string_[:-1]


def get_sum_3(list_: list) -> int:
    sum = 0
    for i in list_:
        if i % 3 == 0:
            sum += i
    return sum


if __name__ == "__main__":
    main()
