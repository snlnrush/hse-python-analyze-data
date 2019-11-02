"""
В csv-файле (разделитель - точка с запятой, кавычки не используются) содержится анонимизированная информация о
зарплатах сотрудников в различных компаниях. В первом столбце записано название компании, а во втором - зарплата.

Поменяйте местами первый и второй столбцы, по-прежнему разделяя значения в ячейках одной строки точкой с запятой.
Сохраняйте порядок строк.

csv-файл доступен по ссылке: https://stepik.org/media/attachments/lesson/258922/input.csv
"""


fin = open('input-258922.csv', 'r', encoding='utf8')

lst = []

for item in fin:
    name, zp = item.split(';')
    lst.append((zp.strip(), name))

fin.close()

fout = open('out-text.txt', 'w', encoding='utf8')

for item in lst:
    print(item[0], item[1], sep=';', file=fout)

fout.close()