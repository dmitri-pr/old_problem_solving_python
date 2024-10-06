fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]
n = int(lines[0])
l = list()

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

for n in range(1, n + 1):
    l.append(fib(n))

fout = open('output.txt', 'w')
#print(n, file=fout)
if len(l) > 0:
    for item in l:
        print(item, end = ' ', file=fout)
fout.close()
