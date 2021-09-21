"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: N/A
"""

import pandas as pd

# get file names:
in_file_ = input('Please enter file name: ')
out_file_ = input('Please output file name: ')


def extractDistrict(name):
    return int(name[:2])


df = pd.read_csv(in_file_)

df['District'] = df['DBN'].apply(extractDistrict)
df.to_csv(out_file_, index=False)

results_ = pd.read_csv(out_file_)
print(results_)
