num1 = int(input())
num2 = int(input())

division = num1 % num2

if division == 0:
    print(f'{num1} делится на {num2} нацело\n'
          f'частное: {num1 // num2}')
else:
    print(f'{num1} не делится на {num2} нацело\n'
          f'неполное частное: {num1 // num2}\n'
          f'остаток: {division}')
          
          
# 8
# 2
# 8 делится на 2 нацело
# частное: 4

# 10
# 3
# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1