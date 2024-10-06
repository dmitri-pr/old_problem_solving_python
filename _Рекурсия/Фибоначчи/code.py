fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]

n = int(lines[0])
if n == 1:
    l = [0]
elif n == 2:
    l = [0, 1]
else:
    l = [0, 1]
    i = 2
    while i <= n - 1:
        l.append(l[i - 1] + l[i - 2])
        i += 1

fout = open('output.txt', 'w')
#print(n, file=fout)
if len(l) > 0:
    for item in l:
        print(item, end = ' ', file=fout)
fout.close()
