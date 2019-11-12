"""
В этой задаче достаточно вам необходимо найти все внутренние ссылки,
которые есть в обеих статьях: https://stepik.org/media/attachments/lesson/258943/Moscow.html и
https://stepik.org/media/attachments/lesson/258944/New-York.html и вывести их в алфавитном порядке по одной в строке.

Обратите внимание, что если ссылка встречается в статье несколько раз, то учитывать ее нужно лишь однажды.
"""
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup


def internal_urls(url):
    set_urls = set()
    resp = urlopen(url)
    html = resp.read().decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            s = link.get('href')
            if s.startswith('/w') and (':' not in s) and (not s.startswith('#')):
                set_urls.add(s)
    return set_urls


lst_urls = list(internal_urls('https://stepik.org/media/attachments/lesson/258943/Moscow.html') &
                internal_urls('https://stepik.org/media/attachments/lesson/258944/New-York.html'))
lst_urls.sort()
for i in lst_urls:
    print(i)
