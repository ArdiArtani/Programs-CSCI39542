"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import pandas as pd

def extractDistrict(name):
    return name[:2]

# get inputs:
ela_file_ = input('Enter file containing ELA scores: ')
math_file_ = input('Enter file containing MATH scores: ')
# ela_file_ = 'ela_trunc.csv'
# math_file_ = 'math_trunc.csv'

# read csv files
df_ela_ = pd.read_csv(ela_file_, index_col=False)
df_math_ = pd.read_csv(ela_file_, index_col=False)

# add subject column
df_ela_['Subject'] = 'ELA'
df_math_['Subject'] = 'MATH'

# concat both csv filess
df_ = [df_ela_, df_math_]
df_ = pd.concat(df_)

# extract district
df_['District'] = df_['DBN'].apply(extractDistrict)

# calculate proficiency
df_['Proficiency'] = (df_['# Level 3+4']/df_['Number Tested']) * 100

#  group and get maxium profiency
df_ = df_.loc[ df_.groupby('District')['Proficiency'].idxmax() ]

# df_.reset_index(inplace=True)


filtered_header_ = ["District", "Subject", "Proficiency", "School Name"]
print(df_[filtered_header_])

# pd.to_csv(df_[filtered_header_], index=False)
