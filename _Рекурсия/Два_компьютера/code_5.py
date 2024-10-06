def sorting():
    global res_
    global res
    global delta
    global delta_supp
    global delta_prev
    global nums_1
    global nums_2
    global nums_supp_1
    global nums_supp_2
    if delta == 0 or delta == delta_prev:
        return None
    else:
        j = None
        q = None
        delta_prev = delta
        delta_supp = delta
        for m, item in enumerate(nums_supp_1):
            for i, el in enumerate(nums_supp_2):
                interim_supp = nums_supp_1[m]
                print(2,interim_supp)
                nums_supp_1[m] = nums_supp_2[i]
                nums_supp_2[i] = interim_supp
                print(2,nums_1)
                print(2,nums_2)
                print(2,nums_supp_1)
                print(2,nums_supp_2)
                if sum(nums_supp_1) - half > 0 and sum(nums_supp_1) - half < delta_supp:
                    delta_supp = sum(nums_supp_1) - half
                    print(333,delta_supp)
                    q = m
                    j = i
                elif sum(nums_supp_2) - half > 0 and sum(nums_supp_2) - half < delta_supp:
                    delta_supp = sum(nums_supp_2) - half
                    print(333,delta_supp)
                    q = m
                    j = i
                elif sum(nums_supp_2) - half == 0 or sum(nums_supp_1) - half == 0:
                    delta = 0
                    print(333,delta)
                    nums_1[m] = nums_supp_1[m]
                    nums_2[i] = nums_supp_2[i]
                    res_ = sum(nums_1)
                    return None
                nums_supp_1 = nums_1.copy()
                nums_supp_2 = nums_2.copy()
                delta = delta_supp

        print(3, delta)
        print(3, nums_1)
        print(3, nums_2)
        print(3, q)
        print(3, j)


        if j != None:
            interim = nums_1[q]
            nums_1[q] = nums_2[j]
            nums_2[j] = interim
            print(4, nums_1)
            print(4, nums_2)
        if delta != 0:
            nums_supp_1 = nums_1.copy()
            nums_supp_2 = nums_2.copy()
            print(4, delta)
            print(4, nums_1)
            print(4, nums_2)
            res_ = max(sum(nums_1), sum(nums_2))
            sorting()

def sorting_():
    global res_
    global res
    global delta
    global res_fin
    global res_fin_prev
    global res_supp
    global res_supp_prev
    global nums_1
    global nums_2
    global nums_supp_1
    global nums_supp_2
    if delta == 0 or res_fin == res_fin_prev:
        return None
    else:
        res_fin_prev = res_fin
        res_supp = 0
        d = 0
        a = None
        b = None
        l = list()
        if len(nums_1) <= len(nums_2) and sum(nums_1) > sum(nums_2):
            for m, item in enumerate(nums_supp_1):
                for i, el in enumerate(nums_supp_2):
                    if nums_supp_1[m] - nums_supp_2[i] > 0:
                        for j in range(i + 1, len(nums_2)):
                            if nums_supp_1[m] - (nums_supp_2[i] + nums_supp_2[j]) > 0 and nums_supp_1[m] - (nums_supp_2[i] + nums_supp_2[j]) < delta:
                                d = nums_supp_1[m] - (nums_supp_2[i] + nums_supp_2[j])
                                nums_supp_2[i] = nums_supp_2[i] + nums_supp_2[j]
                                nums_supp_2[j] = 0
                                res_supp = half + (delta - d)
                                if res_supp < res_supp_prev:
                                    l.clear()
                                    res_supp_prev = res_supp
                                    print('delta - d', delta - d)
                                    print('res_', res_)
                                    print('res_supp_prev', res_supp_prev)
                                    print('res_supp', res_supp)
                                    print('m', m)
                                    print('i', i)
                                    print('j', j)
                                    print('nums_supp_1', nums_supp_1)
                                    print('nums_supp_2', nums_supp_2)
                                    a = m
                                    b = i
                                    if i not in l:
                                        l.append(i)
                                    l.append(j)
                                    print('l', l)
                            elif nums_supp_1[m] - (nums_supp_2[i] + nums_supp_2[i + 1]) == delta:
                                res = half
                                delta = 0
                                return None
                            elif nums_supp_1[m] - (nums_supp_2[i] + nums_supp_2[i + 1]) > delta and nums_supp_1[m] - (nums_supp_2[i] + nums_supp_2[i + 1]) < 2*delta:
                                d = nums_supp_1[m] - (nums_supp_2[i] + nums_supp_2[i + 1])
                                nums_supp_2[i] = nums_supp_2[i] + nums_supp_2[i + 1]
                                nums_supp_2[i + 1] = 0
                                res_supp = half + (d - delta)
                                if res_supp < res_supp_prev:
                                    l.clear()
                                    res_supp_prev = res_supp
                                    print('d', d)
                                    print('d - delta', d - delta)
                                    print('res_', res_)
                                    print('res_supp_prev', res_supp_prev)
                                    print('res_supp', res_supp)
                                    print('m', m)
                                    print('i', i)
                                    print('j', j)
                                    print('nums_supp_1', nums_supp_1)
                                    print('nums_supp_2', nums_supp_2)
                                    a = m
                                    b = i
                                    if i not in l:
                                        l.append(i)
                                    l.append(j)
                                    print('l', l)
                    nums_supp_1 = nums_1.copy()
                    nums_supp_2 = nums_2.copy()

        elif len(nums_1) <= len(nums_2) and sum(nums_1) < sum(nums_2):
            for m, item in enumerate(nums_supp_1):
                for i, el in enumerate(nums_supp_2):
                    if nums_supp_1[m] - nums_supp_2[i] > 0:
                        for j in range(i + 1, len(nums_2)):
                            if (nums_supp_2[i] + nums_supp_2[j]) - nums_supp_1[m] > 0 and (nums_supp_2[i] + nums_supp_2[j]) - nums_supp_1[m] < delta:
                                d = (nums_supp_2[i] + nums_supp_2[j]) - nums_supp_1[m]
                                nums_supp_2[i] = nums_supp_2[i] + nums_supp_2[j]
                                nums_supp_2[j] = 0
                                res_supp = half + (delta - d)
                                if res_supp < res_supp_prev:
                                    l.clear()
                                    res_supp_prev = res_supp
                                    res_fin = res_supp
                                    print('d', d)
                                    print('delta - d', delta - d)
                                    print('res_', res_)
                                    print('res_supp_prev', res_supp_prev)
                                    print('res_supp', res_supp)
                                    print('m', m)
                                    print('i', i)
                                    print('j', j)
                                    print('nums_supp_1', nums_supp_1)
                                    print('nums_supp_2', nums_supp_2)
                                    a = m
                                    b = i
                                    if i not in l:
                                        l.append(i)
                                    l.append(j)
                                    print('l', l)
                            elif (nums_supp_2[i] + nums_supp_2[i + 1]) - nums_supp_1[m] == delta:
                                res = half
                                delta = 0
                                return None
                            elif (nums_supp_2[i] + nums_supp_2[i + 1]) - nums_supp_1[m] > delta and (nums_supp_2[i] + nums_supp_2[i + 1]) - nums_supp_1[m] < 2*delta:
                                d = (nums_supp_2[i] + nums_supp_2[i + 1]) - nums_supp_1[m]
                                nums_supp_2[i] = nums_supp_2[i] + nums_supp_2[i + 1]
                                nums_supp_2[i + 1] = 0
                                res_supp = half + (d - delta)
                                if res_supp < res_supp_prev:
                                    l.clear()
                                    res_supp_prev = res_supp
                                    print('d - delta', d - delta)
                                    print('res_', res_)
                                    print('res_supp_prev', res_supp_prev)
                                    print('res_supp', res_supp)
                                    print('m', m)
                                    print('i', i)
                                    print('j', j)
                                    print('nums_supp_1', nums_supp_1)
                                    print('nums_supp_2', nums_supp_2)
                                    a = m
                                    b = i
                                    if i not in l:
                                        l.append(i)
                                    l.append(j)
                                    print('l', l)
                    nums_supp_1 = nums_1.copy()
                    nums_supp_2 = nums_2.copy()

        print('prefin', nums_1)
        print('prefin', nums_2)
        print('prefin', l)

        if a != None:
            interim = nums_1[a]
            nums_1[a] = 0
            for i, el in enumerate(nums_1):
                if i in l:
                    nums_1.append(nums_2[i])
            for i, el in enumerate(nums_2):
                if i in l:
                    nums_2[i] = 0
            nums_2.append(interim)
            nums_1.sort(reverse=True)
            nums_2.sort(reverse=True)
            delta = max(sum(nums_1), sum(nums_2)) - half
            print('fin', nums_1)
            print('fin', nums_2)
        if delta != 0:
            nums_supp_1 = nums_1.copy()
            nums_supp_2 = nums_2.copy()
            print('fin1', delta)
            print('fin1', nums_1)
            print('fin1', nums_2)
            res_fin = max(sum(nums_1), sum(nums_2))
            sorting_()


fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]
nums = list(map(int, lines[0].split(' ')[1:]))
res_ = 0
res_fin = 0
delta_prev = None
res_supp_prev = None

nums.sort(reverse=True)
k = len(nums)
half = sum(nums)/2

if k == 1:
    res = nums[0]
elif k == 2:
    res = max(nums)
elif k > 2 and nums[0] > sum(nums[1:]):
    res = nums[0]
elif k > 2:
    for i in range(k):
        if sum(nums[0:i+1]) == half:
            res = sum(nums[0:i+1])
            break
        elif sum(nums[0:i+1]) < half and sum(nums[0:i+2]) > half:
            delta = abs(sum(nums[0:i+1]) - half)
            nums_1 = nums[0:i+1]
            nums_2 = nums[i+1:]
            res = sum(nums[i+1:])
            print(1,nums_1)
            print(1,nums_2)
            print(1,delta)
            break
    if res != half:
        nums_1 = nums_1 + [0]*(len(nums_2) - len(nums_1))
        nums_2 = nums_2
        nums_supp_1 = nums_1.copy()
        nums_supp_2 = nums_2.copy()
        sorting()
        nums_supp_1 = nums_1.copy()
        nums_supp_2 = nums_2.copy()
        res_fin = 0
        res_fin_prev = res_
        res_supp_prev = res_
        sorting_()

print('res', res)
if not res_fin and res_:
    print('res_', res_)
    res = res_
elif res_fin and res_:
    print('res_fin', res_fin)
    if res_fin < res_:
        res = res_fin
    else:
        res = res_

res_sum = int(res)

fout = open('output.txt', 'w')
print(res_sum, file=fout)
# if len(lst) > 0:
#     for item in lst:
#         print(item, file=fout)
fout.close()
