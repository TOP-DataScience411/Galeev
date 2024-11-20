def orth_triangle (*, cathetus1: float = 0, cathetus2: float = 0, hypotenuse: float = 0) -> float | None:
    """
    Функция, которая вычисляет третью сторону прямоугольного треугольника по двум переданным, принимает в качестве аргументов длины двух сторон: это могут быть два катета или один из катетов и гипотенуза.
    """
    
    if hypotenuse and (cathetus1 >= hypotenuse or cathetus2 >= hypotenuse):
        return 

    if sum(x > 0 for x in (cathetus1, cathetus2, hypotenuse)) != 2:
        return 
       
    if not hypotenuse:
        return (cathetus1 ** 2 + cathetus2 ** 2) ** 0.5
    
    if not cathetus1:     
        return (hypotenuse ** 2 - cathetus2 ** 2) ** 0.5   
    
    if not cathetus2:      
        return (hypotenuse ** 2 - cathetus1 ** 2) ** 0.5  

# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None        