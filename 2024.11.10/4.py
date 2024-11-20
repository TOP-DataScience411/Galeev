def countable_nouns (num: int, nouns: tuple[str, str, str]) -> str:
    """
    Функция возвращает одно слово из трёх, переданных вторым аргументом, которое согласуется с переданным первым аргументом числом.
    """
    last_two_digits = num % 100 
    last_digit = num % 10  

    if (
           11 <= last_two_digits <= 19 
        or last_digit == 0 
        or 5 <= last_digit <= 9
    ):
        return nouns[2]  
    elif 2 <= last_digit <= 4:
        return nouns[1]  
    elif last_digit == 1:
        return nouns[0]  
        
# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'        