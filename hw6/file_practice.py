"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""

"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""

"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""

"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""

"""
    5.
    В средину файла file_practice.txt вставить строку " *some inserted text* "
    (средина - имеется в виду средина текста)
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def main():
    # 1
    file_path = BASE_DIR / "file_practice.txt"
    file = open(file_path, 'w')
    file.write('Starting practice with files\n')
    file.close()
    # 2
    file = open(file_path, 'r')
    str5 = file.read(5)
    file.seek(0)
    all_str = file.read()
    print(str5.upper() + all_str)
    file.close()
    # 3
    file_path = BASE_DIR / "files" / "text.txt"
    file = open(file_path, 'r')
    all_str = file.read()
    if all_str.count('i') > all_str.count('e'):
        all_str = all_str.replace('i', 'e')
    if all_str.count('e') > all_str.count('i'):
        all_str = all_str.replace('e', 'i')
    file.close()
    file = open(file_path, 'a')
    file.write(all_str)
    file.close()
    # 4
    file_path = BASE_DIR / "file_practice.txt"
    file = open(file_path, 'r')
    all_str = file.read()
    file.close()
    file = open(file_path, 'a+')
    if len(all_str) % 2 == 0:
        file.write('the end\n')
    else:
        file.write('bye\n')
    file.seek(0)
    print(file.read())
    file.close
    # 5
    file = open(file_path, 'r')
    all_str = file.read()
    file.close()

    file = open(file_path, 'w')
    file.write(all_str[:len(all_str) // 2])
    file.write(' *some inserted text* ')
    file.write(all_str[len(all_str) // 2:])
    file.close()


if __name__ == "__main__":
    main()
