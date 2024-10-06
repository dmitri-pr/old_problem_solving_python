def sorting(n):
    global nums
    global supp_list_1
    global supp_list_2
    if n == 1:
        supp_list_1.append(nums[0])
        return nums[0]
    elif n > 1:
        if sum(supp_list_1) <= sum(supp_list_2):
            supp_list_1.append(nums[n - 1])
            return nums[n - 1]
        else:
            supp_list_2.append(nums[n - 1])
            return 0

fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]
nums = list(map(int, lines[0].split(' ')[1:]))

# import numpy as np
#
# import random
# p = random.randint(1, 10)
# nums = list(np.random.randint(1, 20, p))
# print(nums)

nums.sort(reverse=True)
k = len(nums)
supp_list_1 = list()
supp_list_2 = list()
lst = list()

for i in range(1, k + 1):
    lst.append(sorting(i))

print(nums, sum(nums))
print(lst, sum(lst))
print(supp_list_1, sum(supp_list_1))
print(supp_list_2, sum(supp_list_2))

if sum(lst) < sum(supp_list_2):
    res_sum_ = sum(supp_list_2)
else:
    res_sum_ = sum(lst)

res_sum__ = 0
for i in range(k + 1):
    if sum(nums[0:i+1]) <= sum(nums[i+1:]) and sum(nums[i+1:]) - sum(nums[0:i+1]) <= nums[k - 1]:
        res_sum__ = sum(nums[i+1:])
        print(nums[0:i+1], sum(nums[0:i+1]))
        print(nums[i+1:], sum(nums[i+1:]))
        break

if res_sum__ and res_sum__ <= res_sum_:
    res_sum = res_sum__
else:
    res_sum = res_sum_

fout = open('output.txt', 'w')
print(res_sum, file=fout)
# if len(lst) > 0:
#     for item in lst:
#         print(item, file=fout)
fout.close()
