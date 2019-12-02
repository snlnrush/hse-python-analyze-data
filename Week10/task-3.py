"""
Используя модуль xmltodict определите, координаты точек (node) имеющие тег с ключом shop для участка карты.
Выведите координаты в формате, пригодном для вставки в пример leaflet для отображения в виде маркеров,
в том порядке, в котором точки встречаются в исходном файле.

Если вы все делаете правильно, то первые строки в вашем ответе должны быть такими:

L.marker([55.6027557, 37.4934168]).addTo(mymap);
L.marker([55.6034066, 37.4899744]).addTo(mymap);
L.marker([55.6043511, 37.4885361]).addTo(mymap);
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
                print('L.marker([{0}, {1}]).addTo(mymap);'.format(node['@lat'], node['@lon']))
        elif isinstance(node['tag'], list):
            for tag in node['tag']:
                if tag['@k'] == 'shop':
                    count_shops += 1
                    print('L.marker([{0}, {1}]).addTo(mymap);'.format(node['@lat'], node['@lon']))
