"""
Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов,
заключенную между первым и последнием появлением буквы h, в противоположном порядке.

Sample Input:
In the hole in the ground there lived a hobbit
Sample Output:

In th a devil ereht dnuorg eht ni eloh ehobbit
"""
in_str = input()
h1 = in_str.find('h')
h2 = in_str.rfind('h')
mir_str = in_str[h2 - 1: h1: -1]
in_str = in_str.replace(in_str[h1 + 1: h2], mir_str)
print(in_str)
