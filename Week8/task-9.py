"""
Напишите программу, которая будет разрезать большую прямоугольную область на N×N одинаковых прямоугольных областей.
Области задаются четырьмя координатами: минимальной широтой, минимальной долготой,
максимальной широтой, максимальной долготой.

При выводе области должны быть упорядочены по возрастанию минимальной широты,
а в случае равных широт - по возрастанию минимальной долготы.

Гарантируется, что все числа во входных данных положительны.

Sample Input:

41.173 77.23 42.17 79.004
2
Sample Output:

41.173 77.23 41.6715 78.117
41.173 78.117 41.6715 79.004
41.6715 77.23 42.17 78.117
41.6715 78.117 42.17 79.004
"""

min_shir, min_dolg, max_shir, max_dolg = input().split(' ')
n = int(input())
lst_square = []
shag_shir = (float(max_shir) - float(min_shir)) / n
shag_dolg = (float(max_dolg) - float(min_dolg)) / n

for i in range(n):
    for j in range(n):
        mis = float(min_shir) + shag_shir * i
        mid = float(min_dolg) + shag_dolg * j
        mas = float(min_shir) + shag_shir * (i + 1)
        mad = float(min_dolg) + shag_dolg * (j + 1)
        lst_square.append((mis, mid, mas, mad))

lst_square.sort()

for item in lst_square:
    print(*item, end='\n')
