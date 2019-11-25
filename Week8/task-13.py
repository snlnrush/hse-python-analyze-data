"""
Вам дана область карты https://stepik.org/media/attachments/lesson/266078/mapcity.osm

Пройдите по всем way в этой области, выделите среди них замкнутые
(те, у которых совпадает ссылка на первый и последний node), среди всех замкнутых выделите те,
у которых установлен tag с ключом building и произвольным значением.

Для каждого подходящего под условия way выведите две строки. В первой укажите одно число - id этого way.
Во второй перечислите через пробел id (ref) всех nd, входящих в этот way в том же порядке,
в котором они перечисляются в файле.

Выводить ответы для подходящих way нужно в том порядке, в котором они встречаются во входном файле

Если вы все делаете правильно, то ваш ответ должен начинаться со строк

28889642
317555544 317555545 317555546 317555547 317555544
28911067
317558736 529559432 317558559 317558560 317558561 317558562 317558290 529559420 529559416 529559414 529559412 529559410
529559426 529559424 529559422 317558289 317558288 317558736
"""

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/266078/mapcity.osm')
xml = resp.read().decode('utf8')
soup = BeautifulSoup(xml, 'lxml')
nd_start = ''
nd_finish = ''
nd_lst = []

for way in soup.find_all('way'):
    nd_start = way.find_all('nd', limit=1)
    nd_start = nd_start[0]['ref']
    for nd in way.find_all('nd'):
        nd_finish = nd['ref']
    if nd_start == nd_finish:
        for tag in way.find_all('tag', attrs={'k': 'building'}):
            print(way['id'])
            for nd_id in way.find_all('nd'):
                nd_lst.append(nd_id['ref'])
            print(*nd_lst)
            nd_lst.clear()
