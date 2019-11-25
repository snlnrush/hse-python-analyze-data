"""
В файле https://stepik.org/media/attachments/lesson/258944/New-York.html есть несколько таблиц,
у которых атрибут class равен wikitable collapsible collapsed.

Вам необходимо найти первые три такие таблицы и преобразовать их в csv-таблицы.
В csv-таблице ячейки должны разделяться запятой, а строки не должны окружаться кавычками.
Таблицы следует разделять пустой строкой.
Например, для таблиц:

<table>
<tr><td>a</td><td>b</td></tr>
<tr><td colspan=2>c</td></tr>
</table>

<table>
<tr><td>1</td><td>2</td></tr>
</table>
ответ должен выглядеть так:

a,b
c

1,2
Обратите внимание, что в таблице может встречаться тег <tbody>, на который мы можем просто не обращать внимания.
Также там могут встречаться теги <th> (ячейка-заголовок), которые следует интерпретировать так же как теги <td>.
Для поиска нескольких тегов удобно пользоваться методом find_all,
которому в качестве параметра передается список строк с нужными названиями тегов.

Чтобы получить содержимое тега td (то что записано от открывающего до закрывающего тега),
достаточно написать td.text. Лучше удалить все пробельные символы в полученной строке с помощью метода strip().
"""
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup


def internal_urls(url, num_table):
    resp = urlopen(url)
    html = resp.read().decode('utf8')
    soup = BeautifulSoup(html, 'lxml')
    count_table = 1
    table_html = ''
    for link in soup.find_all('table', 'wikitable collapsible collapsed'):
        if count_table == num_table + 1:
            break
        table_html = link
        count_table += 1
    row_text = ''
    for row in table_html.find_all('tr'):
        for col in row.children:
            if col.name is not None:
                row_text += col.text.strip() + ','
        print(row_text[: -1])
        row_text = ''


internal_urls('https://stepik.org/media/attachments/lesson/258944/New-York.html', 1)
print()
internal_urls('https://stepik.org/media/attachments/lesson/258944/New-York.html', 2)
print()
internal_urls('https://stepik.org/media/attachments/lesson/258944/New-York.html', 3)
