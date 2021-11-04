"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: 20.2. Predicting Ice Cream Ratings¶
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# It returns the smallest intger degree >= 1 for which the model yields a MSE of < the specified epsilon.
# Following the textbook code demostration in Lecture 16, write a function that takes values of an independent variable and corresponding values of a dependent varaible, and fits polynomial regression models of increasing degree until the MSE falls below error.
def mse_cost(pred, y):
    return np.mean((pred - y) ** 2)

def fitPoly(df,xes,yes,epsilon=0.01):


    degree_ = 1
    xes_ = df[xes].values.reshape(-1,1)
    yes_ = df[yes].values.reshape(-1,1)

    for i in range(len(df)):
        x_ = PolynomialFeatures(degree=2).fit_transform(xes_)
        clf_ten_ = LinearRegression(fit_intercept=False).fit(x_, yes_)
        pred_ten = clf_ten_.predict(x_)
        mse_ = mse_cost(pred_ten, yes_)

        if(mse_ < epsilon):
            return degree_
        else:
            degree_ += 1



# df = pd.read_csv('icecream.csv')
# print(f'Starting df:\n {df}')
# eps = 0.5
# deg = fitPoly(df,'sweetness','overall',epsilon=eps)
# print(f'For epsilon = {eps}, poly has degree {deg}.')

# For epsilon = 0.5, poly has degree 1.
