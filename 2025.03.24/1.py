from numpy import array
from utility import coef_corr, countable_nouns, find_max_correlation
# Исходные данные с 2012 года
malign = array([50.5, 50.8, 52.0, 53.7, 54.7, 55.6, 56.4, 57.4, 56.3, 57.9, 59.3, 60.5])
invest = array([655061743.4, 699948879.0, 795407850.6, 854288043.8, 873778705.8, 
                  950257084.9, 960689437.2, 1060560377.0, 1091333468.1, 1193578508.5, 1322563915.0])


results, best_shift, max_r = find_max_correlation(malign, invest)

print("Анализ корреляции при разных сдвигах:")
for res in results:
    print(f"\nСдвиг: {res['shift']} {countable_nouns(res['shift'], ("год", "года", "лет"))}")
    print(f"Значения malign: {res['X_values'] * malign.std() + malign.mean()}")
    print(f"Значения invest: {res['Y_values'] * invest.std() + invest.mean()}")
    print(f"Коэффициент корреляции: {res['correlation']:.4f}")

print(f"\nМаксимальная корреляция ({max_r:.4f}) достигается при сдвиге в {best_shift} {countable_nouns(best_shift, ("год", "года", "лет"))}")

  