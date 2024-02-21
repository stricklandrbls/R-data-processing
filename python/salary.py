import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def ReadDataFile(data):
    raw = pd.read_csv(data)
    # x values are YoE (independent)
    x = raw.iloc[:, :-1].values
    # y values are Salaries (dependent)
    y = raw.iloc[:, -1].values
    return x,y

def Regress(x_train,y_train):
    regressor = LinearRegression()
    return regressor.fit(x_train, y_train)

def Plot(regressor, x_train, y_train, x_test, y_test):
    # Points chosen for Test Data Set
    plt.scatter(x_test, y_test, color='red')
    # Points that the regression model were trained with
    plt.scatter(x_train, y_train, color='green')
    # Actual predicted linear regression against trained data
    plt.plot(x_train, regressor.predict(x_train), color = 'blue')
    # plt.plot(x_train[:6], model.predict(myYoeData), color = 'purple')
    plt.title("Predicted Salary for Years of Experience")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.savefig("python/Salaries Regression.png")

def CalculateSlope(regression, x_train):
    y = [regression[0], regression[-1]]
    x = [x_train[0], x_train[-1]]
    delta = [(x[1] - x[0]), (y[1] - y[0])]
    return delta[1] / delta[0]

def main():
    x,y = ReadDataFile("data/Salary_Data.csv")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=12)
    
    # NOTE: THere is no need to apply feature scaling because there is only 1 independent variable.
    #       So there is no need to Standardize or Normalize the data sets.

    print("\tX Train:\n", x_train)
    print("\tX Test:\n", x_test)

    model = Regress(x_train, y_train)
    trainingRegression = model.predict(x_train)
    modelSlope = CalculateSlope(trainingRegression, x_train)
    print("For every additional year of experience, a salary increase of $",modelSlope,"can be expected")
    
main()