import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

def read_transform_set():
    
    rawDataSet = pd.read_csv("data/purchased.csv")

    # Read data set by line with `iloc[]`
    # 2D array where layer[0] is every line and [1] is the array of data values
    #   [
    #       ['france' 44 72000],
    #       ['spain' 27 48000],
    #           etc...
    #   ]
    x = rawDataSet.iloc[:,:-1].values
    y = rawDataSet.iloc[:,-1].values

    # Replace missing salary w/ average of salaries
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

    # "fit" the imputer on every line's column data indexes [1] & [2]
    imputer.fit(x[:, 1:3])
    # Transform and reassign the returned value to `x`
    x[:,1:3] = imputer.transform(x[:, 1:3])

    # Implement One Hot Encoding for Country Category
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
    x = np.array(ct.fit_transform(x))

    # Implement One Hot Encoding for Purchased Category
    le = LabelEncoder()
    y = le.fit_transform(y)

    # Implement Feature Scaling
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)
    sc = StandardScaler()

    x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
    x_test[:, 3:] = sc.transform(x_test[:, 3:])

    print("\nX Training Set\n", x_train)
    print("\nX Test Set\n", x_test)

def perform_simple_linear_regression():
    print()

def main():
    read_transform_set()

main()