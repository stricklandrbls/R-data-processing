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

def main():
    x,y = ReadDataFile("data/Salary_Data.csv")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=12)
    
    # NOTE: THere is no need to apply feature scaling because there is only 1 independent variable.
    #       So there is no need to Standardize or Normalize the data sets.

    print("\tX Train:\n", x_train)
    print("\tX Test:\n", x_test)

    model = Regress(x_train, y_train)
    predictedSalaries = model.predict(x_test)

    for i in range(0, len(x_test)):
        print(x_test[i]," Years of Experience can expect $", predictedSalaries[i])

    # myYoeData = [[0],[5],[10],[15],[16],[17]]

    # Points chosen for Test Data Set
    plt.scatter(x_test, y_test, color='red')
    # Points that the regression model were trained with
    plt.scatter(x_train, y_train, color='green')
    # Actual predicted linear regression against trained data
    plt.plot(x_train, model.predict(x_train), color = 'blue')
    # plt.plot(x_train[:6], model.predict(myYoeData), color = 'purple')
    plt.title("Predicted Salary for Years of Experience")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.savefig("python/Salaries Regression.png")
    # plt.show()

main()