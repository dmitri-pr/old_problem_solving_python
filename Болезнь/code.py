def is_notnull(lst):
    return [i for i, e in enumerate(lst) if e != '0']

def all_indices(lst):
    return [i for i, e in enumerate(lst)]

def count_dict(dict, value):
    count = 0
    l = list()
    for k, v in d.items():
        if v == value:
            count += 1
            l.append(k)
    return (count, l)

fin = open('disease.in', 'r')
lines = [line.strip() for line in fin.readlines()]

n = len(lines[1].replace(' ', '')) - 1
d = dict()
d_temp = dict()
data = False

for line in lines[1:]:
    line = line.replace(' ', '')
    lst = list(line)
    print(lst)
    lst_processed = is_notnull(lst[0:n])
    print(lst_processed)
    if lst[n] == '0':
        for item in lst_processed:
            item += 1
            if not item in d:
                d[item] = '0'
            elif item in d and d[item] == '2':
                d[item] = '0'
            elif item in d and d[item] == '1':
                data = 'Incorrect'
                break
    elif lst[n] == '1' and len(lst_processed) == 1:
        item = lst_processed[0] + 1
        if not item in d:
            d[item] = '1'
        elif item in d and d[item] == '2':
            d[item] = '1'
        elif item in d and d[item] == '0':
            data = 'Incorrect'
            break
#    elif lst[n] == '1' and len(lst_processed) == 0:
#        data = 'Incorrect'
#        break
#    elif lst[n] == '0' and len(lst_processed) == 0:
#        data = 'Incorrect'
#        break
    else:
        count = 0
        x = None
        for item in lst_processed:
            item += 1
            if not item in d:
                d[item] = '2'
                x = item
            elif item in d and d[item] == '0':
                count += 1
        try:
            if len(lst_processed) - count == 1 and x != None:
                d[x] = '1'
        except:
            pass

if not data:
    print('S')
    for line in lines[1:]:
        line = line.replace(' ', '')
        lst = list(line)
        lst_processed = is_notnull(lst[0:n])
        if lst[n] == '1' and len(lst_processed) > 1:
            count = 0
            y = None
            for item in lst_processed:
                item += 1
                if d[item] == '2':
                    y = item
                elif d[item] == '0':
                    count += 1
            try:
                if len(lst_processed) - count == 1 and y != None:
                    d[y] = '1'
            except:
                pass

if not data:
    print('S1')
    for line in lines[1:]:
        line = line.replace(' ', '')
        lst = list(line)
        lst_processed = is_notnull(lst[0:n])
        l = list()
        if lst[n] == '1':
            for item in lst_processed:
                item += 1
                if d[item] == '0':
                    l.append(item -1)
            if lst_processed == l:
                data = 'Incorrect'
                break

if not data:
    d_all = dict()
    for line in lines[1:]:
        line = line.replace(' ', '')
        lst = list(line)
        lst_processed = all_indices(lst[0:n])
        for item in lst_processed:
            item += 1
            if not item in d_all or d_all[item] == '0':
                d_all[item] = line[item - 1]
    for k, v in d_all.items():
        if v == '0':
            d[k] = '2'

#if not data:
#    print('S2')
#    if n - count_dict(d, '0')[0] == 1: # - count_dict(d, '1')[0] == 1:
#        for k, v in d.items():
#            if v == '2':
#                d[k] = '1'

print(d)

fout = open('disease.out', 'w')
if data:
    print(data, file=fout)
else:
    count, l = count_dict(d, '0')
    print(count, end=' ', file=fout)
    print(*l, file=fout)
    count, l = count_dict(d, '1')
    print(count, end= ' ', file=fout)
    print(*l, file=fout)
    count, l = count_dict(d, '2')
    print(count, end=' ', file=fout)
    print(*l, file=fout)
fout.close()
