"""
Некоторый банк хочет внедрить систему управления счетами клиентов, поддерживающую следующие операции:
Пополнение счета клиента. Снятие денег со счета. Запрос остатка средств на счете. Перевод денег между счетами клиентов.
Начисление процентов всем клиентам.
Вам необходимо реализовать такую систему. Клиенты банка идентифицируются именами (уникальная строка, не содержащая пробелов).
Первоначально у банка нет ни одного клиента. Как только для клиента проводится операция пололнения, снятия или перевода денег,
ему заводится счет с нулевым балансом. Все дальнейшие операции проводятся только с этим счетом.
Сумма на счету может быть как положительной, так и отрицательной, при этом всегда является целым числом.
Входной данные содержат количество и последовательность операций. Возможны следующие операции:
DEPOSIT name sum - зачислить сумму sum на счет клиента name. Если у клиента нет счета, то счет создается.
WITHDRAW name sum - снять сумму sum со счета клиента name. Если у клиента нет счета, то счет создается.
BALANCE name - узнать остаток средств на счету клиента name.
TRANSFER name1 name2 sum - перевести сумму sum со счета клиента name1 на счет клиента name2.
Если у какого-либо клиента нет счета, то ему создается счет. INCOME p - начислить всем клиентам,
у которых открыты счета, pот суммы счета. Проценты начисляются только клиентам с положительным остатком на счету,
если у клиента остаток отрицательный, то его счет не меняется. После начисления процентов сумма на счету остается целой,
то есть начисляется только целое число денежных единиц. Дробная часть начисленных процентов отбрасывается.
Для каждого запроса BALANCE программа должна вывести остаток на счету данного клиента.
Если же у клиента с запрашиваемым именем не открыт счет в банке, выведите ERROR.

Sample Input:

7
DEPOSIT Ivanov 100
INCOME 5
BALANCE Ivanov
TRANSFER Ivanov Petrov 50
WITHDRAW Petrov 100
BALANCE Petrov
BALANCE Sidorov

Sample Output:

105
-50
ERROR
"""

n = int(input())
d_clients = {}
for item in range(n):
    lst = [i for i in input().split()]
    if lst[0] == 'DEPOSIT':
        d_clients[lst[1]] = d_clients.get(lst[1], 0) + int(lst[2])
    elif lst[0] == 'WITHDRAW':
        d_clients[lst[1]] = d_clients.get(lst[1], 0) - int(lst[2])
    elif lst[0] == 'TRANSFER':
        d_clients[lst[1]] = d_clients.get(lst[1], 0) - int(lst[3])
        d_clients[lst[2]] = d_clients.get(lst[2], 0) + int(lst[3])
    elif lst[0] == 'INCOME':
        for key, val in d_clients.items():
            if val > 0:
                d_clients[key] = int(val + val * (int(lst[1]) / 100))
    elif lst[0] == 'BALANCE':
        if lst[1] in d_clients:
            print(d_clients[lst[1]])
        else:
            print('ERROR')
