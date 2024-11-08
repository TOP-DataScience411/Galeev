ticket = input()

if (
    int(ticket[0]) + int(ticket[1]) + int(ticket[2]) 
    == 
    int(ticket[3]) + int(ticket[4]) + int(ticket[5])
):
    print('да')
else:
     print('нет')
     
# Второй вариант:     
# r = 0
# l = 0
# for index, i in enumerate(ticket):
    # if index > 2:
        # r += int(i)
    # else:
        # l += int(i)
# print('да' if r == l else 'нет')

# Какой лучше? 

# 183534
# да

# 401367
# нет      