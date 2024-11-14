mail = input()

if '@' in mail:
    if mail.rfind('.') > mail.index('@'):
        print('да')
    else:
        print('нет')    
else:
    print('нет')

# sgd@ya.ru
# да    

# abcde@fghij
# нет