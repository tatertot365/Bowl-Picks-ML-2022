import numpy as np
import statsmodels.api as sm
import pandas as pd

df = pd.read_csv('teams_col_add.csv')
df = df.dropna()

label = 'point_diff'

y = df[label]
X = df.select_dtypes(np.number).assign(cont=1)
X = X.drop(columns = [label])


model1 = sm.OLS(y, X)
results1 = model1.fit()
print(results1.summary())