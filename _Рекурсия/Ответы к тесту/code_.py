import copy

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

right_answ = '+'

k = 0

def matching():
    global res
    global right_answ
    global k
    k += 1
    flag_w = 0
    if k > 2:
        return
    if len(res) == q:
        return
    i = 0
    res_lines_ = copy.deepcopy(res_lines)
    # print('_', res_lines_)
    # print(res_lines)
    for i in range(q):
        for el in res_lines_:
            if el[0][i] == right_answ:
                el[2] += 1
                if el[2] > el[1]:
                    el[2] -= 1
                    el[3] += 1
                    if el[3] <= q - el[1]:
                        if right_answ == '+':
                            right_answ = '-'
                        else:
                            right_answ = '+'
                        flag_w += 1
                        if flag_w > 1:
                            break
                    else:
                        el[3] -= 1
            elif el[0][i] != right_answ:
                el[3] += 1
                if el[3] > q - el[1]:
                    el[3] -= 1
                    if right_answ == '+':
                        right_answ = '-'
                    else:
                        right_answ = '+'
                    flag_w += 1
                    if flag_w > 1:
                        break
        if flag_w <= 1:
            res += right_answ
            flag_w = 0
            i += 1
        else:
            res = ''
            right_answ = '-'
            matching()

if res_lines[0][1] == q:
    res = res_lines[0][0]
else:
    matching()

# print(right_answ)
print(res)

fout = open('output.txt', 'w')
print(res, file=fout)
# if len(lst) > 0:
#     for item in lst:
#         print(item, file=fout)
fout.close()
