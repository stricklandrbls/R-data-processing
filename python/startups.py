# Investors provided a data set for different companies and there expendeture vs profit. The investor wants to know which companies to invest in based on
# what the expendetures are.
# Data Columns: R&D, Admin, Marketing, State, Profit

# The dependent variable would be Profits.
# y = Profit
# Because there are multiple independent variables, we must use the Multivariable Linear Regression model: y = b0 + b1x1 + ... + bnxn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def ReadData(filepath):
    data = pd.read_csv(filepath)
    x = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    return x, y

def EncodeCategoricalData(x):
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
    return np.array(ct.fit_transform(x))

x, y = ReadData("data/startups.csv")
x = EncodeCategoricalData(x)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(x_train, y_train)

profitPredictions = regressor.predict(x_test)
np.set_printoptions(precision=2)

print(np.concatenate((profitPredictions.reshape(len(profitPredictions)), 1), y_test.reshape(len(y_test), 1)), 1)
