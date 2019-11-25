"""
В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте.
Ноды могут не только обозначать какой-то точечный объект,
но и входить в состав way (некоторой линии, возможно замкнутой) и не иметь собственных тегов.
Для доступного по ссылке https://stepik.org/media/attachments/lesson/245681/map2.osm фрагмента карты посчитайте,
сколько всего тегов node встречается на этой карте. В качестве ответа введите одно число.
"""
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm')
xml = resp.read().decode('utf8')
soup = BeautifulSoup(xml, 'lxml')
cnt = 0
for way in soup.find_all('node'):
    cnt += 1
print(cnt)
