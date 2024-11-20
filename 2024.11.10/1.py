def strong_password (password: str) -> bool:
    """
    Пароль считается надёжным, если соблюдены все нижеследующие условия:
    - длина пароля составляет восемь символов и более
    - в пароле присутствуют буквенные символы в обоих регистрах
    - в пароле присутствуют минимум два символа цифр
    - кроме символов букв и цифр в пароле присутствуют символы прочих категорий (пробел, знаки пунктуации, диакритические знаки и т.п.)
    """
    digit_count = 0
    upper_case = 0
    lower_case = 0
    special_char = 0
    
    if len(password) >= 8:
        for i in password:
            if i.isupper():
                upper_case += 1    
            elif i.islower():
                lower_case += 1
            elif i.isdecimal():
                digit_count += 1
            elif not i.isalnum():
                special_char += 1
    
    if (
        upper_case * lower_case * special_char != 0 
        and digit_count > 1
    ):
        return True
    else:
        return False 
        
# Второй вариант:
# def strong_password(password):
#     if len(password) < 8:
#         return False
#     
#     upper_case = any(i.isupper() for i in password)
#     lower_case = any(i.islower() for i in password)
#     special_char = any(not i.isalnum() for i in password)
#     digit_count = sum(i.isdigit() for i in password)
# 
#     return (
#             upper_case 
#         and lower_case 
#         and special_char 
#         and digit_count > 1
#      )

# Какой более оптимизированный?        
        
             

# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password')
# False               