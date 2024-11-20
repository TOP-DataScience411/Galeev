from math import floor

ratio = {}
letters = [
    '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9', 'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z'
]

for l in letters:
    for m in range(0 + letters.index(l), 1 + letters.index(l)):
        ratio[l] = m
        
def decimal_sys (decimal_integer: int, decimal_fractional: float, targ: int) -> str:
    """
    Перевод числа из десятичной системы в целевую систему счисления.
    """
    
    if targ == 10:
        return str(decimal_integer + decimal_fractional)

    result_integer = ''
    
    while decimal_integer > 0:
        decimal_integer, remainder = divmod(decimal_integer, targ)
        result_integer = list(ratio.keys())[remainder] + result_integer
        
    result_fractional = ''
    
    if decimal_fractional:
        for _ in range(6):
            decimal_fractional *= targ
            whole_part = floor(decimal_fractional)
            decimal_fractional -= whole_part
            result_fractional += list(ratio.keys())[whole_part]
            if decimal_fractional == 0:
                break
            
    if result_fractional:
        return result_integer + '.' + result_fractional
    else:        
        return result_integer
    
def int_base (num: str, init: int, targ: int ) -> str:
    """
    Перевод числа из исходной системы счисления в десятичную, а потом в целевую системы счисления.
    """
    
    if not 2 < targ < 36 and not 2 < init < 36:
        return    
    
    if str(init) in ' '.join(num).split():
        return
    
    decimal_fractional = 0
    if '.' in num:
        num, fract = num.split('.')         
        decimal_fractional = sum(
            ratio[ch] * init ** -i 
            for i, ch in enumerate(fract, start=1)
        )
            
    decimal_integer = sum(
        ratio[ch] * init ** i 
        for i, ch in enumerate(num[::-1])
    )
      
    return decimal_sys (decimal_integer, decimal_fractional, targ)

# >>> int_base('ff00.a', 16, 2)
# '1111111100000000.101'
# >>> int_base('ff00.a', 16, 10)
# '65280.625'
# >>> int_base('ff00', 16, 2)
# '1111111100000000'
# >>> int_base('1101010', 2, 30)
# '3g'    
            
            
            