l = [1, 2, 3, 4 , 5]

def rec(i, subset):
    if i == len(l):
        print(subset)
        return

    rec(i + 1, subset + [l[i]])
    rec(i + 1, subset)


rec(0, [])
