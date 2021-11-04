"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import pandas as pd
import numpy as np

# addIndicator(df, colName = "Registration State", indicator = "NY"): This function takes three inputs:
# df: a DataFrame that including the specified column.
# colName: a column name of the specified DataFrame. The default value is Registration State.
# indicator: the value used for the indicator as well as the new column created. The default value is NY.

# The function should add a new column, indicator to the DataFrame that takes values 1 when indicator is in df[colName] and 0 if it has a different value and nanotherwise.
def addIndicator(df, colName = "Registration State", indicator = "NY"):
    df[indicator] = np.where(df[colName] != indicator, 1, 0)
    return df


# df = pd.read_csv('Parking_Violations_Issued_Precinct_19_2021.csv',low_memory=False)
# df['Issue Date'] = pd.to_datetime(df['Issue Date'])
# dff = addIndicator(df)
# print(dff)
# print(f'Of the {len(dff)} violations for first half of 2021 for Upper East Side (PD District 19),\n \
#       {len(dff[dff.NY == 1])} are for cars registered in New York.')
