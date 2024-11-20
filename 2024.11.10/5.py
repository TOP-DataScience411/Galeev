from math import prod

def central_tendency (num1: float, num2: float, *nums: float) -> dict[str, int]:
    """
    Функция возвращает словарь с подписанными вычисленными значениями мер центральной тенденции.

    Ключи словаря:
        'median' — медиана
        'arithmetic' — среднее арифметическое
        'geometric' — среднее геометрическое
        'harmonic' — среднее гармоническое
        """
    nums2 = sorted((num1, num2) + nums)
    length = len(nums2)
    half_l = length // 2
    d = {}
   
    if length % 2 == 0:
        d['median'] = (nums2[half_l] + nums2[half_l - 1]) / 2
    else:
        d['median'] = nums2[half_l]
    
    d['arithmetic'] = sum(nums2) / length
    d['geometric'] = prod(nums2) ** (1 / length)
    d['harmonic'] = length / sum(1 / n for n in nums2)
   
    return d  

# >>> sample = [1.5, 5.9, 1.3, 7.2, 4.0]
# >>> central_tendency(*sample)
# {'median': 4.0, 'arithmetic': 3.9800000000000004, 'geometric': 3.19194810660403, 'harmonic': 2.507173210329423} 
# >>> central_tendency(1.3, .2, .3, 4.5)
# {'median': 0.8, 'arithmetic': 1.575, 'geometric': 0.7697093800545404, 'harmonic': 0.4289642529789184}   

    
        
        
            