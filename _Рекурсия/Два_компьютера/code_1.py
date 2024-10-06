def sorting():
    global g
    global res_
    global res
    global delta
    global nums_1
    global nums_2
    global nums_supp_1
    global nums_supp_2
    if g > len(nums_1):
        return None
    if delta == 0:
        return None
    else:
        for m, item in enumerate(nums_supp_1):
            for i, el in enumerate(nums_supp_2):
                interim_supp = nums_supp_1[m]
                print(2,interim_supp)
                nums_supp_1[m] = nums_supp_2[i]
                nums_supp_2[i] = interim_supp
                print(2,nums_supp_1)
                print(2,nums_supp_2)
                if sum(nums_supp_1) - half > 0 and sum(nums_supp_1) - half < delta:
                    delta = sum(nums_supp_1) - half
                    print(333,delta)
                    nums_1[m] = nums_supp_1[m]
                    nums_2[i] = nums_supp_2[i]
                    nums_supp_1 = nums_1.copy()
                    nums_supp_2 = nums_2.copy()
                    print(5, delta)
                    print(5, nums_1)
                    print(5, nums_2)
                    res_ = max(sum(nums_1), sum(nums_2))
                    g += 1
                    sorting()
                elif sum(nums_supp_2) - half > 0 and sum(nums_supp_2) - half < delta:
                    delta = sum(nums_supp_2) - half
                    print(333,delta)
                    nums_1[m] = nums_supp_1[m]
                    nums_2[i] = nums_supp_2[i]
                    nums_supp_1 = nums_1.copy()
                    nums_supp_2 = nums_2.copy()
                    print(5, delta)
                    print(5, nums_1)
                    print(5, nums_2)
                    res_ = max(sum(nums_1), sum(nums_2))
                    g += 1
                    sorting()
                elif sum(nums_supp_2) - half == 0 or sum(nums_supp_1) - half == 0:
                    delta = 0
                    print(333,delta)
                    nums_1[m] = nums_supp_1[m]
                    nums_2[i] = nums_supp_2[i]
                    res_ = sum(nums_1)
                    break
                nums_supp_1 = nums_1.copy()
                nums_supp_2 = nums_2.copy()
                print(4, delta)
                print(4, nums_1)
                print(4, nums_2)

        #         nums_supp_1 = nums_1.copy()
        #         nums_supp_2 = nums_2.copy()
        #         print(4, delta)
        #         print(4, nums_1)
        #         print(4, nums_2)
        #         res_ = max(sum(nums_1), sum(nums_2))
        # g += 1
        # sorting()

fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]
nums = list(map(int, lines[0].split(' ')[1:]))
res_ = 0
g = 0

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
    for i in range(k + 1):
        if sum(nums[0:i+1]) == half:
            res = sum(nums[0:i+1])
            break
        if sum(nums[0:i+1]) < half and sum(nums[0:i+2]) > half:
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
        nums_supp_1 = nums_1.copy()
        nums_supp_2 = nums_2.copy()
        sorting()
        # for m, item in enumerate(nums_supp_1):
        #     for i, el in enumerate(nums_supp_2):
        #         interim_supp = nums_supp_1[m]
        #         print(2,interim_supp)
        #         nums_supp_1[m] = nums_supp_2[i]
        #         nums_supp_2[i] = interim_supp
        #         print(2,nums_supp_1)
        #         print(2,nums_supp_2)
        #         if sum(nums_supp_1) - half > 0 and sum(nums_supp_1) - half < delta:
        #             delta = sum(nums_supp_1) - half
        #             print(333,delta)
        #             nums_1[m] = nums_supp_1[m]
        #             nums_2[i] = nums_supp_2[i]
        #         elif sum(nums_supp_2) - half > 0 and sum(nums_supp_2) - half < delta:
        #             delta = sum(nums_supp_2) - half
        #             print(333,delta)
        #             nums_1[m] = nums_supp_1[m]
        #             nums_2[i] = nums_supp_2[i]
        #         nums_supp_1 = nums_1.copy()
        #         nums_supp_2 = nums_2.copy()
        #         print(4, delta)
        #         print(4, nums_1)
        #         print(4, nums_2)
        #         res_ = max(sum(nums_1), sum(nums_2))

print(res_)
print(res)
if res_:
    res = res_
res_sum = res

fout = open('output.txt', 'w')
print(res_sum, file=fout)
# if len(lst) > 0:
#     for item in lst:
#         print(item, file=fout)
fout.close()
