"""
Вася составил таблицу с ценами на продукты в разных магазинах.
В первой строке таблицы (кроме первой ячейки) записаны названия продуктов.
Во всех строках, начиная со второй, записана информация о ценах в магазине.
В первой ячейки написано название магазина, а в ячейках, начиная со второй - цена на товар,
название которого записано в первой строке соответствующего столбца.

Таблица задана как csv-файл, разделителем ячеек выступает точка с запятой,
а строковые константы не окружаются кавычками.

Вася очень хочет поесть, но денег у него мало. Поэтому помогите ему определить цену самого дешевого продукта.
В качестве ответа введите одно число.

Ссылка на csv-файл: https://stepik.org/media/attachments/lesson/258925/input.csv
"""

fin = open('input-258925.csv', 'r', encoding='utf8')

lst = []

min_price = 100000

for item in fin.readlines():
    lst = list(item.split(';'))
    for i in lst:
        if i.rstrip().isdigit() and int(i.rstrip()) < min_price:
            min_price = int(i.rstrip())

fin.close()

print(min_price)
