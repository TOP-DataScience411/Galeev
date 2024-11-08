n = int(input())
fibonacci = [0, 1]

for _ in range(n - 1):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

fibonacci.pop(0)    
print(' '.join(map(str, fibonacci)))

# 1
# 1

# 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597    