from numpy import array 
from scipy.stats import norm

def hypo_test(tension, capacity):
    """
    Функция, проверяющая гипотезы:
    1. Крайние члены вариационных рядов нагрузки и несущей способности принадлежат генеральным совокупностям;
    2. Равенство дисперсий и средних значений нагрузки и несущей способности;
    3. Выборка подчиняется нормальному распределению.     
    """
    breakpoint()
    alpha = 0.05 # уровень значимости 
    r_stat_crit_tension = 2.294 
    r_stat_crit_capacity = 2.461
    f_stat_crit = 2.83 # критерий Фишера
    s_stat_crit = 2.07 # критерий Стьюдента
    sm_stat_crit = 0.461 # критерий Смирнова
    
    tension_mean = tension.mean()
    capacity_mean = capacity.mean()
    tension_var = tension.var()
    capacity_var = capacity.var() 
    tension_std = tension.std()
    capacity_std = capacity.std()
    
    # наблюдаемые статистики 
    r_stat_obs_tension_min = abs(tension.min() - tension_mean) / tension_std * (9 / 10)**0.5   
    r_stat_obs_tension_max = abs(tension.max() - tension_mean) / tension_std * (9 / 10)**0.5   
    r_stat_obs_capacity_min = abs(capacity.min() - capacity_mean) / capacity_std * (13 / 14)**0.5   
    r_stat_obs_capacity_max = abs(capacity.max() - capacity_mean) / capacity_std * (13 / 14)**0.5

    print(
      f'Минимальный элемент {tension.min()} ряда нагрузки '
      f'{"является" if r_stat_crit_tension > r_stat_obs_tension_min else "не является"} '
      f'элементом генеральной совокупности'
    )
    
    print(
      f'Максимальный элемент {tension.max()} ряда нагрузки '
      f'{"является" if r_stat_crit_tension > r_stat_obs_tension_max else "не является"} '
      f'элементом генеральной совокупности'
    ) 
    
    print(
      f'Минимальный элемент {capacity.min()} несущей способности '
      f'{"является" if r_stat_crit_capacity > r_stat_obs_capacity_min else "не является"} '
      f'элементом генеральной совокупности'
    )  
    
    print(
      f'Максимальный элемент {capacity.max()} несущей способности '
      f'{"является" if r_stat_crit_capacity > r_stat_obs_capacity_max else "не является"} '
      f'элементом генеральной совокупности'
    )    
       
    
    f_stat_obs = (
      tension_var / capacity_var
      if tension_var > capacity_var else
      capacity_var / tension_var
    )
    
    print(
      f'Дисперсия нагрузки в генеральной совокупности '
      f'{"равна" if f_stat_crit > f_stat_obs else "не равна"} '
      f'дисперсии несущей способности в генеральной совокупности'
    )
    
    s_stat_obs = abs(tension_mean - capacity_mean) / ((9 * tension_var + 13 * capacity_var) / 22)**.5 * (140/24)**.5
    
    print(
      f'Среднее значение нагрузки в генеральной совокупности '
      f'{"равно" if s_stat_crit > s_stat_obs else "не равно"} '
      f'среднему значению несущей способности в генеральной совокупности'
    )
    
    # квантили функции нормального распредления
    F_val_tension = laplace_function(tension)
    F_val_capacity = laplace_function(capacity)
    
    print(
      f'Выборка нагрузки '
      f'{"не противоречит" if sm_stat_crit > method_smirnov(F_val_tension) else "противоречит"} '
      f'нормально закону распредления с вероятностью 95%'
     
    )
    
    print(
      f'Выборка несущей способности '
      f'{"не противоречит" if sm_stat_crit > method_smirnov(F_val_capacity) else "противоречит"} '
      f'нормально закону распредления с вероятностью 95%'
     
    )

def method_smirnov(F):
    """
    Функция, в которой применяется метод Н.В.Смирнова для определения закона распределения выборки.
    На вход подаются значения функции распределения.
    """
    n = len(F)
    u = 1/(12 * n) + sum((el - (2*F.index(el) - 1) / (2 * n))**2 for el in F)
    return u

def laplace_function(X):
    """
    Функция нормального распределения Гаусса-Лапласа.
    Cdf - функция, с помощью которой вычисляется табличное значение.
    """
    val_fun = []
    for el in X:
        f = norm.cdf((el - X.mean()) / X.std())
        val_fun.append(f)
    return val_fun        
    
    
# >>> hypo_test(array([227, 258, 271, 288, 292, 301, 322, 331, 372, 413]), array([371, 379, 388, 396, 395, 406, 460, 408, 409, 411, 419, 424, 441, 397]))
# Минимальный элемент 227 ряда нагрузки является элементом генеральной совокупности
# Максимальный элемент 413 ряда нагрузки является элементом генеральной совокупности
# Минимальный элемент 371 несущей способности является элементом генеральной совокупности
# Максимальный элемент 460 несущей способности является элементом генеральной совокупности
# Дисперсия нагрузки в генеральной совокупности не равна дисперсии несущей способности в генеральной совокупности
# Среднее значение нагрузки в генеральной совокупности не равно среднему значению несущей способности в генеральной совокупности
# Выборка нагрузки не противоречит нормально закону распредления с вероятностью 95%
# Выборка несущей способности противоречит нормально закону распредления с вероятностью 95%    