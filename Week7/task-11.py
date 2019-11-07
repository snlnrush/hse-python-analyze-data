"""
В этой задаче достаточно обернуть в функцию то,
что делает предыдущая и вызвать подсчет числа внутренних ссылок для двух статей:
https://stepik.org/media/attachments/lesson/258943/Moscow.html и
https://stepik.org/media/attachments/lesson/258944/New-York.html

В качестве ответа на задачу введите два числа через пробел.
"""
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup


def internal_urls(url):
    resp = urlopen(url)
    html = resp.read().decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    count = 0
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            s = link.get('href')
            if s.startswith('/w') and (':' not in s) and (not s.startswith('#')):
                count += 1
    return count


print(internal_urls('https://stepik.org/media/attachments/lesson/258943/Moscow.html'),
      internal_urls('https://stepik.org/media/attachments/lesson/258944/New-York.html'))
