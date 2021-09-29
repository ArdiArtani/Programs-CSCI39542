"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import pandas as pd

# get inputs:
input_file_ = input('Enter input file name: ')
output_file_ = input('Enter output file name: ')
grade_ = input('Enter grade: ')
year_ = input('Enter year: ')

# input_file_ = 'public-district-attendance-results-2014-2019.csv'
# output_file_ = 'attendanceThirdGrade2019.csv'
# grade_ = '3'
# year_ = '2018-19'

# read csv files
df = pd.read_csv(input_file_)

# convert to strings
df['Grade'] = df['Grade'].astype(str)

# filter by grade and year
results_ = df[(df.Grade == grade_) & (df.Year == year_)]

# save results
results_.to_csv(output_file_, index=False)
