fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]

string = lines[0]
number = int(string)
l = list()
n = 0
while True:
    if len(string) == 1:
        break

    first_char = string[0]
    count = 0
    for char in string:
        if char == first_char:
            count += 1
    if count == len(string):
        break

    num_interim = 0
    char_to_del = None
    for char in string:
        int_without_char = int(string.replace(char, ''))
        if int_without_char > num_interim:
            num_interim = int_without_char
            char_to_del = char
    string = string.replace(char_to_del, '')

    l.append(string)
    n += 1

fout = open('output.txt', 'w')
print(n, file=fout)
if len(l) > 0:
    for item in l:
        print(item, file=fout)
fout.close()
