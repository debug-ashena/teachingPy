import pandas as pd
import numpy as np

boston=pd.read_csv("Boston.csv")
#boston.head(10)

import statsmodels.api as sm
#______________target selection
target=pd.DataFrame(data=boston.values[:,8] , columns=["medv"])
print(target.head())

#simple Linear Regression
X=boston["lstat"]
y=target["medv"]
X=sm.add_constant(X)

model=sm.OLS(y.astype(float),X.astype(float)).fit()
prediction=model.predict(X)
#print(prediction)
#print(model.summary())

#simple Linear Regression multi variable

X2=boston[["black","lstat"]]
y2=target["medv"]
X2=sm.add_constant(X2)

model2=sm.OLS(y2.astype(float), X2.astype(float)).fit()
prediction2=model2.predict(X2)
print(prediction2)
print(model2.summary())
