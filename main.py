"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""

import pandas as pd
# import numpy as np
# import seaborn as sns

# Write a function that will find the columns with highest absolute correlation coefficents in a DataFrame. Your program should take as inputs the column of interest, a list of possible correlated columns, and the DataFrame. The function should return the name and Pearson's R correlation coefficent (can be computed using the Pandas function series1.corr(series2) where series1 and series2 are Pandas Series):


# This function takes three inputs: colName: a column name of the specified DataFrame,
# colList: a list of column names of the specified DataFrame. It must be a list and assumed to be non-empty. Can include colName, and
# df: a DataFrame including the specified columns.
# The function computes the correlation coefficient between df[colName] and each column specified in colList, and returns the name and the correlation coefficient for the column from the list with the highest absolute value.
def findHighestCorr(colName,colLst,df):

    cor_results_ = []
    for col_name_ in colLst:
        if(colName != col_name_):
            cor_results_.append(df[colName].corr(df[col_name_]))

    return cor_results_
