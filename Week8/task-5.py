"""
В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте.
Ноды могут не только обозначать какой-то точечный объект,
но и входить в состав way (некоторой линии, возможно замкнутой) и не иметь собственных тегов.
Для доступного по ссылке https://stepik.org/media/attachments/lesson/245681/map2.osm фрагмента карты посчитайте,
сколько всего тегов node не содержат в себе ни одного тега tag (первое число в ответе),
а сколько содержит хотя бы один тег tag (второе число в ответе). Числа введите через пробел.
"""

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm')
xml = resp.read().decode('utf8')
soup = BeautifulSoup(xml, 'lxml')
count_yes = 0
count_no = 0
for way in soup.find_all('node'):
    if way.tag is None:
        count_no += 1
    else:
        count_yes += 1

print(count_no, count_yes)
