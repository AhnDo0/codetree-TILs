N = int(input())
nums = []
num_in_use = []
count = 0
max_count = 0

for i in range(N):
    num = int(input())
    if num not in num_in_use:
        num_in_use.append(num)
    nums.append(num)

#K를 배열에서 제거
#연속하여 동일한 숫자가 나오는지

temp = nums[0]
for i in num_in_use:
    new_nums = [x for x in nums if x != i]

    count = 0
    temp = new_nums[0]
    for j in new_nums:
        if temp == j:
            count += 1
        else:
            count = 1
            temp = j
        if max_count < count:
            max_count = count
            k = i
print(max_count)