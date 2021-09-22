"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: From textbook.ds100.org: 6.3 SQL Joins
"""

import pandas as pd
import pandasql as psql

# get file names:
# input_file_ = input('Please enter input file name: ')
# output_file_ = input('Please enter output file name: ')

input_file_ = "mta_trunc_staten_island.csv"
output_file_ = "filteredSI.csv"

# read csv file
df_ = pd.read_csv(input_file_)

results_ = df_.groupby(['date']).agg(
    {'entries': 'sum', 'exits': 'sum'}).reset_index()

results_.to_csv(output_file_, index=False)

# date,entries,exits
# 2020-01-01,3128,0
# 2020-01-02,13707,0
# 2020-01-03,12507,23
