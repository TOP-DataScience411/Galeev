def numbers_strip (numbers: list[float], n: int = 1, *, copy: bool = False) -> list:
    """
    Функция, которая удаляет n минимальных и n максимальных чисел из списка, принимает обязательным аргументом список вещественных чисел, необязательными аргументами число n и переключатель вернуть исходный список или копию.
    """
    numbers_copy = numbers.copy() if copy else numbers
    
    for _ in range(n):
        numbers_copy.remove(max(numbers_copy))
        numbers_copy.remove(min(numbers_copy))       
    
    return numbers_copy 
    

# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample
# [2, 3]
# >>> sample is sample_stripped
# True
# >>>
# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [30]
# >>> sample is sample_stripped
# False        