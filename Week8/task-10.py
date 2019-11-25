
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm')
xml = resp.read().decode('utf8')
soup = BeautifulSoup(xml, 'lxml')
count_fuel = 0

for way in soup.find_all('way'):
    for tag in way.find_all('tag', attrs={'v': 'fuel', 'k': 'amenity'}):
        count_fuel += 1

for node in soup.find_all('node'):
    for tag in node.find_all('tag', attrs={'v': 'fuel', 'k': 'amenity'}):
        count_fuel += 1

print(count_fuel)
