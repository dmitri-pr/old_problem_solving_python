def sorting(l, n):
    if n == len(l):
        return [[]]
    lst = list()
    addItem = l[n]
    ll = l
    for x in sorting(ll, n + 1):
        lst.append([addItem] + x)
    for x in sorting(ll, n + 1):
        lst.append(x)
    return lst

fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]
nums = list(map(int, lines[0].split(' ')[1:]))

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
    total = sum(nums)
    min_diff = sum(nums)
    best_sum = 0
    for item in sorting(nums, 0):
        item_sum = sum(item)
        if abs(item_sum - (total - item_sum)) < min_diff:
            min_diff = abs(item_sum - (total - item_sum))
            best_sum = item_sum
    if best_sum > total/2:
        res = best_sum
    else:
        res = sum(nums) - best_sum

print(res)


fout = open('output.txt', 'w')
print(res, file=fout)
# if len(lst) > 0:
#     for item in lst:
#         print(item, file=fout)
fout.close()
