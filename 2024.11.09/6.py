binary_num = input()
j = set()
b = {'b'}

for i in binary_num:
    j.add(i)

if j.isdisjoint(b):
    print('да')
else:
    print('нет')  

# 1b0101
# нет    