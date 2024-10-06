def sorting(l, n):
    if n == len(l):
        return [0]
    lst = list()
    addItem = l[n]
    ll = l
    for x in sorting(ll, n + 1):
        lst.append(addItem + x)
        lst.append(x)

    return lst

fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]
nums = list(map(int, lines[0].split(' ')[1:]))

nums.sort(reverse=True)
k = len(nums)
half = sum(nums)/2
res = 0

if k == 1:
    res = nums[0]
elif k == 2:
    res = max(nums)
elif k > 2 and nums[0] > sum(nums[1:]):
    res = nums[0]
if k > 2 and not res:
    for i in range(k + 1):
        if sum(nums[0:i+1]) == half:
            res = sum(nums[0:i+1])
            break
if k > 2 and not res:
    total = sum(nums)
    l = sorting(nums, 0)
    l.sort(reverse=True)
    for m, item in enumerate(l):
        if m < len(l) - 1:
            # if sum(l[m]) < half and sum(l[m + 1]) > half:
            #     if half - sum(l[m]) < sum(l[m + 1]) - half:
            #         res = total - sum(l[m])
            #         break
            #     else:
            #         res = sum(l[m + 1])
            #         break
            if l[m] > half and l[m + 1] < half:
                if l[m] - half < half - l[m + 1]:
                    res = l[m]
                    break
                elif l[m] - half == half - l[m + 1]:
                    res = l[m]
                    break
                else:
                    res = total - l[m + 1]
                    break
if k > 2 and not res:
    total = sum(nums)
    l = sorting(nums, 0)
    min_diff = total
    best_sum = 0
    for item in l:
        if abs(item - (total - item)) < min_diff:
            min_diff = abs(item - (total - item))
            best_sum = item
    if best_sum > total/2:
        res = best_sum
    else:
        res = total - best_sum

print(res)


fout = open('output.txt', 'w')
print(res, file=fout)
# if len(lst) > 0:
#     for item in lst:
#         print(item, file=fout)
fout.close()
