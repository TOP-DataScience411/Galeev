from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import BaggingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from pandas import DataFrame, Series
from matplotlib import pyplot as plt
from pathlib import Path 
from sys import path
from numpy import array

dir_path = Path(path[0])

data = load_breast_cancer()

features = DataFrame(data['data'], columns=data['feature_names'])

target = Series(data['target'], name='target')

# >>> target.value_counts()
# target
# 1    357 - доброкачественная опухоль 
# 0    212 - злокачественная опухоль

features_norm = (features - features.describe().loc['mean']) / features.describe().loc['std']

mean_0 = features_norm.loc[target==0].mean()
mean_1 = features_norm.loc[target==1].mean()

diff_mean = DataFrame({
        'mean 0': mean_0,
        'mean 1': mean_1,
        'diff': abs(mean_0 - mean_1)
}).sort_values(by='diff', ascending=False)

bins = 30

# fig, axs = plt.subplots(figsize=(12,8))

# for el in diff_mean.index[:12]:
    # axs.clear()
    # axs.hist(
        # features_norm.loc[target==0, el], 
        # bins=bins, 
        # alpha=0.5, 
        # label='(0) злокачественная'
        # )    
    # axs.hist(
        # features_norm.loc[target==1, el], 
        # bins=bins, 
        # alpha=0.5, 
        # label='(1) доброкачественная'
        # )
    # axs.set(xlabel=el, ylabel='Количество значений в интервале')
    # axs.set_title(f'diff = {round(diff_mean.loc[el ,'diff'], 2)}')    
    # axs.legend()
    # fig.savefig(dir_path/f'breast_cancer-{el}.png', dpi=150)    
    
x_train, x_test, y_train, y_test = train_test_split(
        features_norm[diff_mean.index[:25]], 
        target, 
        test_size=0.2, 
        random_state=1
        ) 
          
model = BaggingClassifier(estimator=LogisticRegression(), n_estimators=50, n_jobs=-1) 
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
        
conf_matrix = confusion_matrix(y_test, y_pred)

# >>> conf_matrix
# array([[40,  2],
       # [ 0, 72]]) 2 - ложноположительные
       
print(f'accuracy = {accuracy_score(y_test, y_pred):.2f}')

# accuracy = 0.98