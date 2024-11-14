fruits = []

while True:
    fruit = input()
    if fruit == '':
        break    
    fruit += ','
    fruits.append(fruit)
    
last = len(fruits) -1
penult = len(fruits) - 2    
fruits[penult] = fruits[penult].strip(',') + ' и'
fruits[last] = fruits[last].strip('и,')

print(' '.join(fruits))

# яблоко
# 
# яблоко

# яблоко
# груша
# 
# яблоко и груша

# яблоко
# груша
# апельсин
# 
# яблоко, груша и апельсин

# яблоко
# груша
# апельсин
# лимон
# 
# яблоко, груша, апельсин и лимон