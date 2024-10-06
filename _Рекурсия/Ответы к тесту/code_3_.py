def matching(n):
    if n == q + 1:
        return ['']
    lst = list()
    for x in matching(n + 1):
        lst.append(x + '+')
        lst.append(x + '-')
    return lst

fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]
res_lines = list()
for i, item in enumerate(lines):
    if i >= 1 and i%2 != 0:
        lst = [lines[i], int(lines[i+1])]
        res_lines.append(lst)
# res_lines = sorted(res_lines, reverse=True, key=lambda x: x[1])
# print(res_lines)

q = int(lines[0].split()[1])
p = int(lines[0].split()[0])
res = ''

vars = matching(1)
# print(vars)

for k in range(len(vars)):
    flag = 0
    for n in range(len(res_lines)):
        if len([(i, el) for i, el in enumerate(vars[k]) if vars[k][i] == res_lines[n][0][i]]) == res_lines[n][1]:
            flag += 1
    if flag == p:
        res = vars[k]
        break

# if not res:
#     res = res_lines[0][0]

print(res)

fout = open('output.txt', 'w')
print(res, file=fout)
# if len(lst) > 0:
#     for item in lst:
#         print(item, file=fout)
fout.close()
