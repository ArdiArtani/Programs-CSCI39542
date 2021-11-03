"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import pandas as pd
import numpy as np
# import scipy.stats as st

# fitPoly(df,xes,yes,epsilon=0.01): This function takes four inputs:
# df: a DataFrame that including the specified columns.
# xes: a column name of the specified DataFrame,
# yes: a column name of the specified DataFrame.
# epsilon: the size of the sample. It has a default value of 0.01.
# It returns the smallest intger degree >= 1 for which the model yields a MSE of < the specified epsilon.

# Following the textbook code demostration in Lecture 16, write a function that takes values of an independent variable and corresponding values of a dependent varaible, and fits polynomial regression models of increasing degree until the MSE falls below error.
def fitPoly(df,xes,yes,epsilon=0.01):
    # df[xes]
    # df[yes]
    deg_ = 1

    return deg_


# df = pd.read_csv('icecream.csv')
# print(f'Starting df:\n {df}')
# eps = 0.5
# deg = fitPoly(df,'sweetness','overall',epsilon=eps)
# print(f'For epsilon = {eps}, poly has degree {deg}.')

# For epsilon = 0.5, poly has degree 1.
