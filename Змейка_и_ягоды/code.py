fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]

print(int(lines[0]))

count = 1
g = 2
result = list()
while count <= int(lines[0]):
    print(count)
    n = int(lines[g - 1].split(' ')[1])
    print('i', g)
    print('n', n)
    m_max = n - 1
    print('n_', n)
    k_max = int(lines[g - 1].split(' ')[0]) - 1
    field = list()
    snake = list()
    for j in range(g, g + n):
        field.append(list(lines[j]))
    print(field)
    brk = False
    for m in range(len(field)):
        if '#' in field[m]:
            print(m)
            print('#' in field[m])
            for k in range(len(field[m])):
                if field[m][k] == '#':
                    m = m
                    k = k
                    brk = True
                    break
            if brk == True:
                break
    print(m, k)
    snake.append((m, k))
    steps = list(lines[g + n])
    print(steps)
    berry_count = 0
    brk = False
    for item in steps:
        if item == 'U':
            m -= 1
        elif item == 'D':
            m += 1
        elif item == 'L':
            k -= 1
        elif item == 'R':
            k += 1
        if m > m_max or m < 0 or k > k_max or k < 0 or (m, k) in snake:
            result.append(-1)
            brk = True
            break
        elif field[m][k] == '.':
            for i in reversed(range(1, len(snake))):
                snake[i] = snake[i - 1]
            snake[0] = (m, k)
        elif field[m][k] == '*':
            berry_count += 1
            last = snake[len(snake) - 1]
            for i in reversed(range(1, len(snake))):
                snake[i] = snake[i - 1]
            snake[0] = (m, k)
            snake.append(last)
        print(m, k)
    count += 1
    print('n__', n)
    print('ii', g)
    g = g + n + 2
    print('iii', g)
    if brk == True:
        continue
    else:
        result.append(berry_count)


fout = open('output.txt', 'w')
#print(count, file=fout)
for item in result:
    print(item, file=fout)
fout.close()
