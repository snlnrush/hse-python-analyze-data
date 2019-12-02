"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет - не выводите ничего. Если таких пар соседей несколько
- выведите первую пару.

Sample Input:

-1 2 3 -1 -2
Sample Output:

2 3
"""
lst_numbers = [int(i) for i in input().split()]
for i in range(1, len(lst_numbers)):
    if lst_numbers[i] < 0 and lst_numbers[i - 1] < 0:
        print(lst_numbers[i - 1], lst_numbers[i])
        break
    elif lst_numbers[i] > 0 and lst_numbers[i - 1] > 0:
        print(lst_numbers[i - 1], lst_numbers[i])
        break
