num = int(input())
print(f'Сумма цифр = {(num // 100) + (num // 10 % 10) + (num % 10)}\nПроизведение цифр = {(num // 100) * (num // 10 % 10) * (num % 10)}')
# 333
# Сумма цифр = 9
# Произведение цифр = 27