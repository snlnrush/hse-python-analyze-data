"""
Используя модуль xmltodict определите, сколько точек (node) имеют тег с ключом shop для участка карты.

Обратите внимание, что в зависимости от количества тегов tag внутри тега node представление информации для тегов
будет либо словарем, либо списком словарей. Чтобы проверить,
что объект является списком можно воспользоваться функцией isinstance:

if isinstance(tag, list):
    print('list')
elif isinstance(tag, dict):
    print('dict')

Не забудьте также, что node может и вовсе не иметь тегов tag внутри себя.
"""
import xmltodict


fin = open('map.osm', 'r', encoding='utf8')
xmltext = fin.read()
fin.close()
xml = xmltodict.parse(xmltext)
count_shops = 0
for node in xml['osm']['node']:
    if 'tag' in node:
        if isinstance(node['tag'], dict):
            if node['tag']['@k'] == 'shop':
                count_shops += 1
        elif isinstance(node['tag'], list):
            for tag in node['tag']:
                if tag['@k'] == 'shop':
                    count_shops += 1

print(count_shops)
