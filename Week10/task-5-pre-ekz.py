"""
В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами доступа к файлам.
Для каждого файла известно, с какими действиями можно к нему обращаться:
запись W,
чтение R,
запуск X.
Вам требуется восстановить контроль над правами доступа к файлам
(ваша программа для каждого запроса должна будет возвращать OK если над файлом выполняется допустимая операция,
или же Access denied, если операция недопустима.

В первой строке входного файла содержится число N (1  N  10000) —
количество файлов содержащихся в данной файловой системе.

В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами.
Длина имени файла не превышает 15 символов.

Далее указано чиcло M (1  M  50000) — количество запросов к файлам.

В последних M строках указан запрос вида Операция Файл.
К одному и тому же файлу может быть применено любое колличество запросов.
Операция чтения обозначается как read, записи - write, запуска - execute.

Для каждого из M запросов нужно вывести в отдельной строке Access denied или OK.

Sample Input:
4
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
5
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog
Sample Output:

OK
Access denied
Access denied
OK
OK
"""
n_files = int(input())
accesses_dict = {}
translate_dict = {'write': 'W', 'read': 'R', 'execute': 'X'}

for file in range(n_files):
    lst_temp = [i for i in input().split()]
    accesses_dict[lst_temp[0]] = lst_temp[1: len(lst_temp)]
    lst_temp.clear()

n_oper = int(input())

for oper in range(n_oper):
    access, file_name = input().split()
    if translate_dict[access] in accesses_dict[file_name]:
        print('OK')
    else:
        print('Access denied')
