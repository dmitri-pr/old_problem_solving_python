fin = open('numbers.in', 'r')
lines = [line.strip() for line in fin.readlines()]
num = lines[0][1:4]
let = lines[0][0:1] + lines[0][4:]
num_list = list()
let_list = list()
lst = list()
n = 6

def var_n(n):
    if n == 1:
        return num
    if n%2 == 0:
        return list(var_n(n - 1))[2] + list(var_n(n - 1))[1] + list(var_n(n - 1))[0]
    if n%2 != 0:
        return list(var_n(n - 1))[0] + list(var_n(n - 1))[2] + list(var_n(n - 1))[1]

def var_l(n):
    if n == 1:
        return let
    if n%2 == 0:
        return list(var_l(n - 1))[2] + list(var_l(n - 1))[1] + list(var_l(n - 1))[0]
    if n%2 != 0:
        return list(var_l(n - 1))[0] + list(var_l(n - 1))[2] + list(var_l(n - 1))[1]

for n in range(1, n + 1):
    if var_n(n) not in num_list:
        num_list.append(var_n(n))

for n in range(1, n + 1):
    if var_l(n) not in let_list:
        let_list.append(var_l(n))

print(num_list)
print(let_list)

for item in let_list:
    for el in num_list:
        lst.append(item[0] + el +item[1:])

print(lst)

k = len(num_list)*len(let_list)

fout = open('numbers.out', 'w')
print(k, file=fout)
if len(lst) > 0:
    for item in lst:
        print(item, file=fout)
fout.close()
