fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]
n = int(lines[0])
l = list()

def fib(n):
    global l
    i = len(l)
    if i > n - 1:
        return l
    if i == 0:
        l.append(0)
    if i == 1:
        l.append(1)
    if i > 1:
        l.append(l[i - 1] + l[i - 2])
    fib(n)

fib(n)

fout = open('output.txt', 'w')
#print(n, file=fout)
if len(l) > 0:
    for item in l:
        print(item, end = ' ', file=fout)
fout.close()
