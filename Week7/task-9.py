"""
Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python.
В этой статье есть теги code, которыми выделяются конструкции на языке Python.
Вам нужно найти все строки, содержащиеся между тегами <code> и </code> и найти те строки,
которые встречаются чаще всего и вывести их в алфавитном порядке, разделяя пробелами.

Например, если исходный текст страницы выглядел бы так:

<code>a</code>
<a>bracadabr</a>
<code>c</code>
<code>b</code>
<code>b</code>
<code>c</code>
то в ответ надо было бы ввести строку "b c".
"""
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

dict_str = {}
lst_pair = []

resp = urlopen(' https://stepik.org/media/attachments/lesson/209719/2.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('code'):
    key = link.text
    dict_str[key] = dict_str.get(key, 0) + 1

for key, val in dict_str.items():
    lst_pair.append((val, key))

lst_pair.sort()
lst_pair.sort(key=lambda x: x[0], reverse=True)

start_key = lst_pair[0][0]
for item in lst_pair:
    if item[0] == start_key:
        print(item[1], '', end='')
    else:
        break
