"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import pandas as pd

def extractDistrict(name):
    return name[:2]

# get inputs:
# ela_file_ = input('Enter file containing ELA scores: ')
# math_file_ = input('Enter file containing MATH scores: ')
ela_file_ = 'ela_trunc.csv'
math_file_ = 'math_trunc.csv'

# read csv files
df_ela_ = pd.read_csv(ela_file_, index_col=False)
df_math_ = pd.read_csv(ela_file_, index_col=False)

# extract district
df_ela_['District'] = df_ela_['DBN'].apply(extractDistrict)
df_math_['District'] = df_math_['DBN'].apply(extractDistrict)

# calculate proficiency
df_ela_['Proficiency'] = (df_ela_['# Level 3+4']/df_ela_['Number Tested']) * 100
df_math_['Proficiency'] = (df_math_['# Level 3+4']/df_math_['Number Tested']) * 100

#  group and get maxium profiency
df_ela_ = df_ela_.loc[ df_ela_.groupby('District')['Proficiency'].idxmax() ]
df_math_ = df_math_.loc[ df_math_.groupby('District')['Proficiency'].idxmax() ]

# add subject column
df_ela_['Subject'] = 'ELA'
df_math_['Subject'] = 'MATH'

# concat both csv filess
df_ = [df_ela_, df_math_]
df_ = pd.concat(df_, axis=0)

filtered_header_ = ["District", "Subject", "Proficiency", "School Name"]
print(df_[filtered_header_])
