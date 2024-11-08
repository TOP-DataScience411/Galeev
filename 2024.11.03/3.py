num = int(input())
result = 0
 

for i in range(num//2):
    if num % (i + 1) == 0:
        result += (i + 1)

print(result + num)    
                
    
# 50
# 93    