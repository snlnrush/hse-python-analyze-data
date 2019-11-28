"""
По данным портала открытых данных Москвы определите количество дней, когда освещение включено 12 часов или более.
"""
import json
from urllib.request import urlopen, urlretrieve


response = urlopen('https://apidata.mos.ru/v1/datasets/3288/rows?api_key=fdd76fdd0fe1d96dceece2e877753135')
resp_data = response.read().decode('utf-8')
lst_json = json.loads(resp_data)

count_days = 0
for item in lst_json:
    h, min = item['Cells']['DurationOfLighting'].split(':')
    if int(h) >= 12:
        count_days += 1
print(count_days)
