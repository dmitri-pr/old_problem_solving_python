fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]
res_lines = list()
for i, item in enumerate(lines):
    if i >= 1 and i%2 != 0:
        lst = [lines[i], int(lines[i+1])]
        res_lines.append(lst)
res_lines = sorted(res_lines, reverse=True, key=lambda x: x[1])
print(res_lines)

q = int(lines[0].split()[1])
p = int(lines[0].split()[0])

res = ''
best_test = list(res_lines[0][0])
l_wrong = list()

def matching(n):
    global l_wrong
    lst = list()
    if n == p:
        return
    if l_wrong == []:
        l_wrong = [(i, el) for i, el in enumerate(best_test)]
    lst = [(i, el) for i, el in enumerate(best_test) if best_test[i] == list(res_lines[n][0])[i]]
    print(best_test)
    print(list(res_lines[n][0]))
    print(lst)
    if len(lst) == q - res_lines[0][1] + res_lines[n][1]:
        l_wrong = list(set(l_wrong) & set(lst))
        print('pr', l_wrong)
    if len(res_lines) == 2 and res_lines[0][1] == res_lines[n][1] and len(lst) == res_lines[0][1] - 1:
        l_wrong = []
        l_supp = [(i, el) for i, el in enumerate(best_test)]
        for item in l_supp:
            if item not in lst:
                l_wrong.append(item)
        print('pr', l_wrong)        
    matching(n + 1)
    return

if res_lines[0][1] == q:
    res = res_lines[0][0]
elif len(res_lines) == 1:
    if res_lines[0][1] != 0:
        res = res_lines[0][0]
    else:
        for j,item in enumerate(best_test):
            if item == '+':
                best_test[j] = '-'
            else:
                best_test[j] = '+'
        res = ''.join(best_test)

if not res:
    matching(1)
    if len(l_wrong) != 0:
        count = 0
        max = q - res_lines[0][1]
        for k, item in enumerate(best_test):
            if count == max: break
            for m, item in enumerate(l_wrong):
                if count == max: break
                if k in item:
                    if item[1] == '+':
                        best_test[k] = '-'
                    else:
                        best_test[k] = '+'
                    count += 1
        res = ''.join(best_test)
    else:
        res = res_lines[0][0]

print(l_wrong)
print(best_test)
print(res)

fout = open('output.txt', 'w')
print(res, file=fout)
# if len(lst) > 0:
#     for item in lst:
#         print(item, file=fout)
fout.close()
