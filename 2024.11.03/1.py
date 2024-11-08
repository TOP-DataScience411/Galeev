nums = []

while True:
    num = int(input())
    if num % 7 == 0:
        num = str(num)
        nums.append(num)
    else:
        nums.reverse()
        print(' '.join(nums))
        break 

# 7
# 7
# 14
# 21
# 13
# 21 14 7 7        