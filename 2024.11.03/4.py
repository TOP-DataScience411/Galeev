n = int(input())
primes = 0
start = 10 ** (n - 1)
end = 10 ** n

for i in range(start, end):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes += 1

print(primes)  

# 3
# 143      