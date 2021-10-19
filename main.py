"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: stackoverflow
"""
import pandas as pd

# uniqueVals: a sorted list of the unique values from the input parameter vals, and
# mass: the fraction that each uniqueVals occurs in vals.
def pmf(vals):
    uniqueVals_ = list(set(vals))
    mass_ = []

    if (isinstance(vals, pd.core.series.Series)):
        vals = vals.tolist()
    else:
        vals = vals

    for val_ in uniqueVals_:
        mass_.append(vals.count(val_) / len(vals))

    return uniqueVals_, mass_


# senators = pd.read_csv('senatorsAges.csv')
# x, y = pmf(senators['age'])
# x, y = pmf([50,50,52,54])
# print(f'The values are: {x}')
# print(f'The pmf is: {y}')
# print(f'The sum of the pmf is: {sum(y)}.')

# The values are: (50, 52, 54)
# The pmf is: (0.5, 0.25, 0.25)
# The sum of the pmf is: 1.0.
