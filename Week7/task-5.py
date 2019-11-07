"""
Мы сохранили страницу с википедии про языки программирования и сохранили
по адресу https://stepik.org/media/attachments/lesson/209717/1.html

Скачайте её с помощью скрипта на Питоне и посчитайте, какой язык упоминается чаще Python или
C++ (ответ должен быть одной из этих двух строк).
Необходимо просто подсчитать количество вхождений слова Python или C++ как подстроки.
"""

from urllib.request import urlopen

response = urlopen('https://stepik.org/media/attachments/lesson/209717/1.html')
html = response.read().decode('utf8')
if html.count('Python') > html.count('C++'):
    print('Python')
else:
    print('C++')
