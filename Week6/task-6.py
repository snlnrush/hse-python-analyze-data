"""
В качестве ответа введите все строки наибольшей длины из входного файла, не меняя их порядок.
В данной задаче удобно считать список строк входного файла целиком при помощи метода readlines().
Ссылка на входной файл: https://stepik.org/media/attachments/lesson/258920/input.txt

Пример входного файла:

One
Twenty one
Two
Twenty two
Пример ответа:

Twenty one
Twenty two
"""

fin = open('input-258920.txt', 'r', encoding='utf8')
max_len = 0
for item in fin.readlines():
    if len(item) > max_len:
        max_len = len(item)
fin.close()
fin = open('input-258920.txt', 'r', encoding='utf8')
for item in fin.readlines():
    if len(item) == max_len:
        print(item)
fin.close()
