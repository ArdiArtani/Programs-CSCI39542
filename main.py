"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""

import pandas as pd
# import seaborn as sns
# import numpy as np

# Write a function that will find the columns with highest absolute correlation coefficents in a DataFrame. Your program should take as inputs the column of interest, a list of possible correlated columns, and the DataFrame. The function should return the name and Pearson's R correlation coefficent (can be computed using the Pandas function series1.corr(series2) where series1 and series2 are Pandas Series):


# This function takes three inputs: colName: a column name of the specified DataFrame,
# colList: a list of column names of the specified DataFrame. It must be a list and assumed to be non-empty. Can include colName, and
# df: a DataFrame including the specified columns.
# The function computes the correlation coefficient between df[colName] and each column specified in colList, and returns the name and the correlation coefficient for the column from the list with the highest absolute value.
def findHighestCorr(colName,colLst,df):

    cor_results_ = []
    for col_name_ in colLst:
        if(colName != col_name_):
            cor_results_.append(df[colName].corr(df[col_name_])).abs()

    return cor_results_

# simpleDF = pd.DataFrame({'c1': [1,2,3,4],\
#                          'c2': [0,1,0,1],\
#                          'c3': [1,10,3,20],\
#                          'c4': [-10,-20,-30,-40],})
# print('Testing with c1 and [c3,c4]:')
# print(p23.findHighestCorr('c1',['c3','c4'],simpleDF))
# print(f'c1 has highest absolute r with {p23.findHighestCorr("c1",simpleDF.columns, simpleDF)}.')
#
#
# tips = sns.load_dataset('tips')
# print(f"Correlation coefficient between tips and size is \
#         {tips['tip'].corr(tips['size'])}")
# print(f"For tip, the highest correlation is \
#         {p23.findHighestCorr('tip',['total_bill','size'],tips)}.")
