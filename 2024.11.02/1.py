num1 = input()
num2 = input()
num3 = input()

result = 0

if '-' not in num1:
    result += float(num1)
if '-' not in num2:
    result += float(num2)
if '-' not in num3:
    result += float(num3)

print(result)

# 4
# -22
# 1.5
# 5.5