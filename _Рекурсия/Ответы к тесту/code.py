fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]
res_lines = list()
for i, item in enumerate(lines):
    if i >= 1 and i%2 != 0:
        lst = [lines[i], int(lines[i+1]), 0, 0]
        res_lines.append(lst)
res_lines = sorted(res_lines, reverse=True, key=lambda x: x[1])
print(res_lines)

q = int(lines[0].split()[1])
p = int(lines[0].split()[0])

res = ''
flag_w = 0

i = 0
while i < q:
    if res_lines[0][1] == q:
        res = res_lines[0][0]
        break
    right_answ = '+'
    for el in res_lines:
        if el[0][i] == right_answ:
            el[2] += 1
            if el[2] > el[1]:
                el[2] -= 1
                el[3] += 1
                if el[3] <= q - el[1]:
                    right_answ = '-'
                    flag_w += 1
                else:
                    el[3] -= 1
        elif el[0][i] != right_answ:
            el[3] += 1
            if el[3] > q - el[1]:
                el[3] -= 1
                right_answ = '-'
                flag_w += 1
    if flag_w == 0:
        res += '+'
    else:
        res += '-'
    flag_w = 0
    i += 1

print(res)

fout = open('output.txt', 'w')
print(res, file=fout)
# if len(lst) > 0:
#     for item in lst:
#         print(item, file=fout)
fout.close()
