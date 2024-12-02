def check(l):
    nums = [int(x) for x in l.split(' ')]
    sign = 0
    for i in range(len(nums)):
        if i == 0:
            sign = nums[1] - nums[0]
            if sign == 0:
                return False
            sign = abs(sign) / sign
            if sign == 0:
                return False
        else:
            s = nums[i] - nums[i-1]
            if abs(s) > 3 or abs(s) < 1:
                return False
            if abs(s) / s != sign:
                return False
    return True

count = 0

with open("input.txt") as file:
    for l in file:
        if check(l):
            count += 1

print(count)
