from pandas import read_csv
from pathlib import Path 
from sys import path
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor 
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression, Ridge
from numpy import array
from pandas import DataFrame


script_dir = Path(path[0])

data = read_csv(script_dir/'boston.csv', comment='#')

# удаление выбросов
data = data.drop(index=data[data['MEDV'] == 50].index)

corr_matrix_pearson = data.corr('pearson').round(2)
corr_matrix_spearman = data.corr('spearman').round(2)

fig = plt.figure(figsize=(50, 8))
axs = fig.subplots(1,13)

for i, el in enumerate(data.columns[:13]):
    axs[i].scatter(data[el], data['MEDV'])
    axs[i].set_title(f'p={corr_matrix_pearson.loc[el, 'MEDV']}\n'
                     f's={corr_matrix_spearman.loc[el,'MEDV']}'
    )
    axs[i].set(
        xticks=[],
        yticks=[],
        xlabel=el,
        ylabel='MEDV'
    )
   

# fig.savefig(script_dir/'boston_corr.png', dpi=100)



x_train, x_test, y_train, y_test = train_test_split(
            data.loc[:, ['CRIM', 'INDUS', 'RM', 'AGE', 'LSTAT']] ,
            data['MEDV'],
            test_size=0.2,
            random_state=1
)

model_1st_lvl = [
    KNeighborsRegressor(n_neighbors=3),
    Ridge(),
    DecisionTreeRegressor(max_depth=5),
    RandomForestRegressor(n_estimators=60, max_depth=6)
]

model_2nd_lvl = LinearRegression()

pred_1st_lvl = []
accuracy_1st_lvl = []

for model in model_1st_lvl:
    model.fit(x_train, y_train)
    pred_1st_lvl.append(model.predict(x_test))
    score = round(model.score(x_test, y_test), 2)
    accuracy_1st_lvl.append(score)
    print(f'accuracy {str(model)} = {score}') 
 
    
pred_1st_lvl = DataFrame(array(pred_1st_lvl).T) 
   
x_train, x_test, y_train, y_test = train_test_split(
        pred_1st_lvl,
        y_test,
        test_size=0.2,
        random_state=1
        )

   
model_2nd_lvl.fit(x_train, y_train)
model_2nd_lvl.predict(x_test)
print(f'\naccuracy {str(model_2nd_lvl)} = {round(model_2nd_lvl.score(x_test,  y_test), 2)}')  

# accuracy KNeighborsRegressor(n_neighbors=3) = 0.58
# accuracy Ridge() = 0.67
# accuracy DecisionTreeRegressor(max_depth=5) = 0.79
# accuracy RandomForestRegressor(max_depth=6, n_estimators=60) = 0.8

# accuracy LinearRegression() = 0.94

 