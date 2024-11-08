letter = input()
result = 0

for i in letter:
    if not i == ' ':
        result += 30
        
r, k = divmod(result, 100)
print(f'{r} руб. {k} коп.')        
        