def product (iterable: float) -> float:
    """
    Рекурсивная функция, которая возвращает произведение чисел.    
    """
    if not iterable:
        return 1.0
        
    if iterable[0] == 0:
        return 0.0
        
    return abs(iterable[0] * product(iterable[1:]))

# >>> product(range(10, 60, 10))
# 12000000.0
# >>> product((0.12, 0.05, -0.09, 0.0, 0.21))
# 0.0        
    
        
                   
            
       
