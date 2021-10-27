"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import pandas as pd
# import seaborn as sns

# Write a function that computes the range of values a column takes (i.e. the difference between the maximum and minimum values). The column contains numeric values, unless the flag datetime is set to True. If the datetime flag is true, the input column contains strings representing datetime objects ( overview of datetime in Pandas ) and the function should return the range in seconds.
def colRange(df, colName, datetime=False):

    if(datetime == False):
        return (df[colName].max() - df[colName].min())
    else:
        df['date'] = pd.to_datetime(df[colName])
        results_ = (df['date'].max() - df['date'].min()).total_seconds()
        return results_



# taxis = sns.load_dataset('taxis').dropna().loc[:10]
# print(f"Testing colRange(taxis,'distance'): {colRange(taxis,'distance')}")
# print(f"Testing colRange(taxis,'dropoff',datetime=True): {colRange(taxis,'dropoff',datetime=True)}")

# Testing colRange(taxis,'distance'): 7.21
# Testing colRange(taxis,'dropoff',datetime=True): 2236694.0
