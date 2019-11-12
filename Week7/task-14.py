"""
В файле https://stepik.org/media/attachments/lesson/209723/3.html находится одна таблица.
Просуммируйте все числа в ней и введите в качестве ответа одно число - эту сумму.
Для доступа к ячейкам используйте возможности BeautifulSoup.
"""

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup


def internal_urls(url):
    resp = urlopen(url)
    html = resp.read().decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    sum_num = 0
    for link in soup.find_all('td'):
        if link.text is not None:
            sum_num += int(link.text)
    return sum_num


print(internal_urls('https://stepik.org/media/attachments/lesson/209723/3.html'))
