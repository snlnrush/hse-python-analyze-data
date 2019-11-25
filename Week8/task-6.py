"""
В OpenStreetMap XML встречаются теги way, которые соответствуют некоторым линиям и многоугольникам на карте.
Way состоит из списка нодов (точек), которые задаются тегами nd вложенными в тег way.
Для доступного по ссылке https://stepik.org/media/attachments/lesson/245681/map2.osm определите id того way,
который содержит в себе наибольшее количество нодов. Если таких несколько - выведите тот id,
который встречается в файле раньше.
"""
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm')
xml = resp.read().decode('utf8')
soup = BeautifulSoup(xml, 'lxml')
way_nd_dict = {}
max_nd = 0
for way in soup.find_all('way'):
    way_id = way['id']
    count_nd = 0
    for nd in way.find_all('nd'):
        count_nd += 1
    if count_nd > max_nd:
        max_nd = count_nd
        way_nd_dict[way_id] = count_nd

lst_way = list(way_nd_dict.items())
lst_way.sort(key=lambda x: x[1])

print(lst_way[-1][0])
