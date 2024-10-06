def isint(char):
    try:
        int(char)
        return True
    except ValueError:
        return False

str = ''
d = dict()
l = list()

fin = open('schools.in', 'r')
lines = [line.strip() for line in fin.readlines()]
for i in range(1, int(lines[0]) + 1):
    for char in lines[i]:
        if isint(char):
            str += char
    if not str in d:
        d[str] = 1
    else:
        d[str] += 1
    str = ''

count = 0
for k, v in d.items():
    if v <= 5:
        count += 1
        l.append(k)

fout = open('schools.out', 'w')
print(count, file=fout)
for item in l:
    print(item, file=fout)
fout.close()
