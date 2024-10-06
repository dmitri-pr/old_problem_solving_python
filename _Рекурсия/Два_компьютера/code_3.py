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

fin = open('input.txt', 'r')
lines = [line.strip() for line in fin.readlines()]
nums = list(map(int, lines[0].split(' ')[1:]))
res_ = 0
delta_prev = None

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
        nums_1 = nums_1 + [0]*(len(nums_2) - len(nums_1))*2
        nums_2 = nums_2 + [0]*5        
        nums_supp_1 = nums_1.copy()
        nums_supp_2 = nums_2.copy()
        sorting()

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
