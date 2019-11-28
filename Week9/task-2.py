"""
В этой задаче необходимо проверить, что у вас установлен и работает модуль json
(обычно он есть в стандартной поставке и не требует дополнительных действий для установки).
Для этого вам необходимо скачать файл с данными и запустить скрипт, сохраненный в той же папке:

import json

fin = open('input.json', 'r', encoding='utf8')
dct = json.loads(fin.read())
fin.close()
popup = dct['menu']['popup']
menuitem = popup['menuitem']
for now in menuitem:
    for key in sorted(now):
        print(key, now[key])
В качестве ответа на задачу сдайте вывод этого скрипта
"""

import json

fin = open('input.json', 'r', encoding='utf8')
dct = json.loads(fin.read())
fin.close()
popup = dct['menu']['popup']
menuitem = popup['menuitem']
for now in menuitem:
    for key in sorted(now):
        print(key, now[key])
