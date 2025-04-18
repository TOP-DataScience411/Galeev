from numpy import array
from matplotlib import pyplot as plt
from time import sleep
from utility import coef_corr, countable_nouns, find_max_correlation
from sys import path 
from pathlib import Path


oil_prices = array([
    381.8, 364.9, 424.5, 390.4, 456.9, 453.8, 430.1, 373.0, 330.9, 344.4,
    323.6, 287.7, 237.0, 207.2, 243.7, 270.2, 305.1, 341.4, 327.6, 303.5,
    332.0, 333.8, 328.4, 349.1, 383.5, 388.7, 381.5, 365.3, 351.9, 354.9,
    333.3, 365.5, 378.3, 405.6, 435.2, 456.5, 485.5, 483.7, 456.6, 480.3,
    524.7, 549.1, 536.8, 518.7, 543.5, 592.1, 535.8, 441.4, 408.4, 450.4,
    475.0, 503.9, 527.3, 486.6, 462.1, 448.5, 434.5, 438.6, 447.7, 471.2,
    477.6, 419.7, 345.1
])
dizel_prices = array([
    34.43, 34.16, 34.14, 34.34, 34.36, 34.42, 34.60, 34.67, 34.73, 34.73,
    35.25, 35.55, 35.54, 35.41, 35.31, 35.25, 35.15, 35.25, 35.54, 35.56,
    35.52, 35.49, 35.76, 36.35, 37.35, 37.60, 37.66, 37.60, 37.62, 37.91,
    38.03, 38.09, 38.13, 38.31, 39.00, 40.03, 40.76, 41.00, 40.96, 41.25,
    42.41, 44.44, 44.48, 44.47, 44.45, 44.81, 45.29, 46.58, 47.22, 47.12,
    46.96, 46.41, 45.99, 46.05, 46.10, 46.14, 46.15, 46.24, 46.97, 47.68,
    48.04, 48.15, 48.11, 47.84, 47.72, 47.78, 48.02, 48.04, 48.04, 48.07,
    48.41, 48.62, 48.84, 49.09, 49.30, 49.53, 49.55, 49.77, 50.12, 50.59,
    50.63, 50.69, 52.10, 53.64, 54.37, 54.78, 54.97, 54.62, 54.50, 54.40,
    54.40, 54.47, 54.76, 55.11, 55.95, 57.83, 58.81, 58.68, 58.38, 58.22,
    58.10, 58.21, 58.42, 59.27, 62.64, 64.39, 64.06, 64.33, 64.46, 64.85,
    64.74, 65.08, 65.21, 65.51, 66.15, 66.71
])

results, best_shift, max_r = find_max_correlation(dizel_prices, oil_prices, max_shift=10)

print("Анализ корреляции при разных сдвигах:")
for res in results:
    print(f"\nСдвиг: {res['shift']} {countable_nouns(res['shift'], ("месяц", "месяца", "месяцев"))}")
    print(f"Значения dizel_prices: {res['X_values'] * dizel_prices.std() + dizel_prices.mean()}")
    print(f"Значения oil_prices: {res['Y_values'] * oil_prices.std() + oil_prices.mean()}")
    print(f"Коэффициент корреляции: {res['correlation']:.4f}")

print(f"\nМаксимальная корреляция ({max_r:.4f}) достигается при сдвиге в {best_shift} {countable_nouns(best_shift, ("месяц", "месяца", "месяцев"))}")

fig = plt.figure(figsize=(8,8))
axs = fig.subplots()

sample_dizel_prices = dizel_prices[best_shift:len(oil_prices)+best_shift]  
sample_oil_prices = oil_prices[:len(dizel_prices)-best_shift]

norm_dizel_prices = (sample_dizel_prices - sample_dizel_prices.mean()) / sample_dizel_prices.std()
norm_oil_prices = (sample_oil_prices - sample_oil_prices.mean()) / sample_oil_prices.std()

intercept = norm_dizel_prices.mean() - max_r * norm_oil_prices.mean()

print(f'Уравнение теоретической линии регресси: y = {max_r: .4f}x + ({intercept: .16f})')

axs.axline((norm_dizel_prices.mean(), norm_oil_prices.mean()), slope=max_r)
axs.scatter(norm_dizel_prices, norm_oil_prices)
axs.scatter(norm_dizel_prices.mean(), norm_oil_prices.mean(), s=250, marker='p')



fig.show()
fig.savefig(Path(path[0]) / 'linear_regres.png' , dpi=300)