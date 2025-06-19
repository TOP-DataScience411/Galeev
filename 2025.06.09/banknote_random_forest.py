from matplotlib import pyplot as plt
from pathlib import Path 
from sys import path 
from pandas import read_csv
from itertools import combinations
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, recall_score, accuracy_score, precision_score


script_dir = Path(path[0])
data = read_csv(script_dir/'banknote-auth.csv')

# fig = plt.figure(figsize=(20,5))
# axs = fig.subplots(1,6)


# for i, el in enumerate(combinations(data.loc[:, :'entropy'], 2)):
    # axs[i].scatter(data[el[0]], data[el[1]])
    # axs[i].set(
        # xticks=[],
        # yticks=[],
        # xlabel=el[0],
        # ylabel=el[1]
        # )
   
    
# fig.show()    

# 0 — поддельная — отрицательный
# 1 — подлинная  — положительный

x_train, x_test, y_train, y_test = train_test_split(
        data.loc[:, :'entropy'], 
        data['class'],
        test_size=1/3,
        random_state=1
        )

model = RandomForestClassifier(
    n_estimators=100, 
    max_depth=5, 
    n_jobs=-1,
    # class_weight='balanced'
)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
conf_matrix = confusion_matrix(y_pred, y_test)

# >>> conf_matrix
# array([[260,   0],
       # [  4, 194]])
       
# >>> y_test.value_counts()
# class
# 0    264
# 1    194 

print(f'accuracy = {accuracy_score(y_test, y_pred):.2f}'
      f'\nrecall = {recall_score(y_test, y_pred):.2f}'  
      f'\nprecision = {precision_score(y_test, y_pred):.2f}'  
) 

# accuracy = 0.99
# recall = 1.00 
# precision = 0.97    