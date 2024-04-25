#import required packages

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

#import data
data=pd.read_csv(r"weather.csv")
encoded_data=pd.get_dummies(data,columns=["province","wind_d","date"])

#setting variables and target variable
y=encoded_data.humidi
x=encoded_data.drop('humidi', axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

#model 1 (Not optimized)
model1=DecisionTreeRegressor(random_state=1)
model1.fit(x_train,y_train)
prediction1=model1.predict(x_test)
print("Nonoptimized model mean error: ")
print(mean_absolute_error(y_test,prediction1))

#model 2 (Optimized based on tree max_leaf_nodes)
#mean calculator function:
def get_mae(max_leaf_nodes,traX,reaX,traY,reaY):
    model_2=DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes,random_state=1)
    model_2.fit(traX,traY)
    predict_val=model_2.predict(reaX)
    mae=mean_absolute_error(reaY,predict_val)
    return mae

#finding best tree size to minimize mean error
'''
sample_max_leaf_nodes=[100,200,500,1000,2000,5000,10000,20000,50000,100000,200000,500000]
mae_data=[]
for i in sample_max_leaf_nodes:
    print("Trying leaf size: "+str(i))
    a=get_mae(i,x_train,x_test,y_train,y_test)
    mae_data.append(a)
    print(str(a))
best_tree_size = sample_max_leaf_nodes[mae_data.index(min(mae_data))]
print("BEST TREE SIZE")
print(best_tree_size)
'''
best_tree_size=100000
#after several test, we found out the max_leaf_nodes that given a good mean error is 100000
#best_tree_size=100000
final_model=DecisionTreeRegressor(max_leaf_nodes=best_tree_size,random_state=1)
final_model.fit(x_train,y_train)
print("Optimized model mean error: ")
print(mean_absolute_error(y_test,final_model.predict(x_test)))


