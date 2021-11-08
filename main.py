"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: stackoveflow
"""
import pandas as pd
import numpy as np

# Write a program that takes a DataFrame of restaurants and returns a DataFrame with each Restaurant occurring exactly once and two new columns: Number_Submissions which contains the number of times that restaurant occurs in any entry (smallest value is 1) and Locations, a list consisting of the unique location addresses.

# dba: where dba is the input parameter above. This column holds the establishment names and is the column to which groupby is applied.
# Num_Submissions: a column that contains a count for each establishment name.
# Locations: a column name that contains for each establishment, a list of unique locations.
def restaurantLocs(df, dba="Restaurant Name", location="Business Address"):
    dba_ = []
    num_submissions_ = []
    locations_ = []

    new_df_ = df.groupby(dba)
    for rname_ , data_ in new_df_:
      dba_.append(rname_)
      num_submissions_.append(data_.shape[0])
      locations_.append(list(set(data_[location])))

    data = {"dba" : dba_, "Num_Submissions" : num_submissions_, "Locations" : locations_}
    results_ = pd.DataFrame(data)
    return results_


# df = pd.read_csv('applications_coffee_truncated.csv')
# print(df)
# newDF = restaurantLocs(df)
# print(newDF)
