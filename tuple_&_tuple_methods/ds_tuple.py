#df.shape
import pandas as pd
data={'name':['kavi','priya'],'mark':[76,90]}
df=pd.DataFrame(data)
print(df.shape)
rows,cols=df.shape
print(rows)
print(cols)

#zip
features=('age','income','score')
importance=(0.8,0.7,0.6)
for feat, imp in zip(features,importance):
    print(feat,":",imp)

#train test split - unpacking
from sklearn.model_selection import train_test_split
x=[1,2,3,4,5]
y=[1,5,6,7,8]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
print(x_train)
print(x_test)
print(y_train)
print(y_test)