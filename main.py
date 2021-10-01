"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: stackoverflow, python, geeksforgeeks
"""
import pandas as pd
def extractDistrict(name):
    return str(name[:2])

# read csv files
df_ela_ = pd.read_csv("ela_trunc.csv", index_col=False)
df_math_ = pd.read_csv("math_trunc.csv", index_col=False)

# add subject column
df_ela_['Subject'] = 'ELA'
df_math_['Subject'] = 'MATH'

# extract district
df_ela_['District'] = df_ela_['DBN'].apply(extractDistrict)
df_math_['District'] = df_math_['DBN'].apply(extractDistrict)

# calculate proficiency
df_ela_['Proficiency'] = (df_ela_['# Level 3+4']/df_ela_['Number Tested']) * 100
df_math_['Proficiency'] = (df_math_['# Level 3+4']/df_math_['Number Tested']) * 100

# add in the schools column
df_ela_['School Name'] = df_ela_['School Name']
df_math_['School Name'] = df_math_['School Name']

#  group and get maxium profiency
df_ela_ = df_ela_.loc[ df_ela_.groupby('District')['Proficiency'].idxmax() ]
df_math_ = df_math_.loc[ df_math_.groupby('District')['Proficiency'].idxmax() ]

# reindex both csv files
df1_ = df_ela_.reindex(columns = ['District', 'Subject', 'Proficiency', 'School Name'])
df2_ = df_math_.reindex(columns = ['District', 'Subject', 'Proficiency', 'School Name'])

# concat both csv filess
df = pd.concat([df1_,df2_], axis=0)

# create pivot table
df_ = pd.pivot_table(df, index=['District','Subject'], aggfunc=max)
print(df_)
