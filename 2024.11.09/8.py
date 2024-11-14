files = input().split('; ')
file_count = {}
result = []

for f in files:
    if f in file_count:
        file_count[f] += 1
        new_name = f.replace('.', f'_{file_count[f]}.', 1)
    else:
        file_count[f] = 1
        new_name = f
    
    if new_name not in result:
        result.append(new_name)

result = sorted(result)
print('\n'.join(result))              
           
# 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main_3.cpp
# src.tar.gz
# src_2.tar.gz                                