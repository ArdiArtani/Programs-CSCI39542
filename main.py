"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""

import pandas as pd
import numpy as np

# This function takes three inputs: colName: a column name of the specified DataFrame,
# colList: a list of column names of the specified DataFrame. It must be a list and assumed to be non-empty. Can include colName, and
# df: a DataFrame including the specified columns.
# The function computes the correlation coefficient between df[colName] and each column specified in colList, and returns the name and the correlation coefficient for the column from the list with the highest absolute value.


def findHighestCorr(colName, colLst, df):

    corr_results_ = []
    for col_name_ in colLst:
        corr_results_.append(df[colName].corr(df[col_name_]))

    highest_value_ = abs(np.max(corr_results_))
    return (colLst[corr_results_.index(highest_value_)], highest_value_)


# simpleDF = pd.DataFrame({'c1': [1, 2, 3, 4],
#                          'c2': [0, 1, 0, 1],
#                          'c3': [1, 10, 3, 20],
#                          'c4': [-10, -20, -30, -40], })
# print('Testing with c1 and [c3,c4]:')
# print(findHighestCorr('c1', ['c3', 'c4'], simpleDF))
# print(
#     f'c1 has highest absolute r with {findHighestCorr("c1",simpleDF.columns, simpleDF)}.')

# Testing with c1 and [c3,c4]:
# ('c4', -1.0)
# c1 has highest absolute r with ('c1', 1.0)
