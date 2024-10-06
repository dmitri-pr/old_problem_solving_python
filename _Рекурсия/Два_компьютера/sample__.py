def sorting(l, n):
    if n == len(l):
        return [0]
    lst = list()
    addItem = l[n]
    ll = l
    for x in sorting(ll, n + 1):
        lst.append(addItem + x)
    for x in sorting(ll, n + 1):
        lst.append(x)
    print(lst)
    return lst


lst = list()
l = [7, 10, 3, 5, 6]


for item in sorting(l, 0):
    print(item)
