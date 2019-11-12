"""
В файле https://stepik.org/media/attachments/lesson/209723/5.html находится одна таблица.
Просуммируйте все числа в ней. Теперь мы не только добавили разных тегов для изменения стиля отображения,
но и сделали невалидный HTML-код (правда, браузеры его отображают, а вот с BeautifulSoup могут быть проблемы).
Невалидный HTML-код - не редкость в интернете, надо учиться работать и с этим.

Вы можете исправить html-код или попробовать использовать нестандартный парсер html,
такой как html5lib (вместо html.parser).
"""
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup


def internal_urls(url):
    resp = urlopen(url)
    html = resp.read().decode('utf8')
    soup = BeautifulSoup(html, 'lxml')
    sum_num = 0
    for link in soup.find_all('td'):
        if link.text is not None:
            sum_num += int(link.text)
    return sum_num


print(internal_urls('https://stepik.org/media/attachments/lesson/209723/5.html'))
