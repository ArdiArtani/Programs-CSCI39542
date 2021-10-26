"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import pandas as pd
from sklearn import linear_model

# the name of a CSV file that will be loaded into a dataframe,
# the name of a column to be used as an independent variable in the multiple linear regression,
# the name of second column to be used as another independent variable in the multiple linear regression,
# the name of a column to be used as an dependent variable in the multiple linear regression (i.e. what is being predicted),
# a value for the first variable, and
# a value for the second variable.

# get file names:
csv_file_ = input('Enter name of CSV: ')
ind_var_ = input('Enter name of first independent variable: ')
ind_var2_ = input('Enter name of second independent variable: ')
name_var_ = input('Enter name of the dependent variable:')
pre_var_ = input('Enter value for first variable for prediction ')
pre_var2_ = input('Enter value for second variable for prediction ')

# Your program should build a linear model based on the dataframe and two independent variables that will predict the value of the dependent variable. Your program should then predict the dependent variable, based on the two inputted independent variables.

# csv_file_ = "mpg.csv"
# ind_var_ = "displacement"
# ind_var2_ = "acceleration"
# name_var_ = "mpq"
# pre_var_ = 100
# pre_var2_ = 12.0

regr = csv_file_.LinearRegression()
regr.fit(mpg[[ind_var_, ind_var2_]], mpg[name_var_])
print (f'Predicted mpg: {regr.predict([[pre_var_,pre_var2_]])[0]}')
