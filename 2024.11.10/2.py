def taxi_cost (route: int, wait: int = 0) -> int | None:
    """
    Расчёт стоимости осуществляется по следующим правилам:
    - базовая стоимость поездки 80 рублей
    - за каждые 150 метров к стоимости добавляется 6 рублей
    - за каждую минуту ожидания к стоимости добавляется 3 рубля
    - при отмене поездки (длина маршрута составила 0 метров) к стоимости добавляется штраф 80 рублей и стоимость времени ожидания
    - итоговая стоимость математически округляется до целого числа
    """
    base_cost = 80
    wait *= 3
    route = route / 150 * 6
    
    if route == 0:
       return base_cost + wait + 80
    elif wait < 0 or route < 0:
        return 
    
    return round(base_cost + wait + route)

# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))
# None  


  