"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
# import matplotlib.pyplot as plt


# Section 16.1 (Random Variables) of the textbook has a small example of computing the probability mass function of a data set of ages was computed by hand. Write a function that will automate this process:

# uniqueVals: a sorted list of the unique values from the input parameter vals, and
# mass: the fraction that each uniqueVals occurs in vals.
def pmf(vals):
    uniqueVals_ = set(vals)
    mass_ = []
    for val_ in uniqueVals_:
        mass_.append(vals.count(val_) / len(vals))

    return uniqueVals_, mass_

x, y = pmf([50,50,52,54])
print(f'The values are: {x}')
print(f'The pmf is: {y}')
print(f'The sum of the pmf is: {sum(y)}.')
plt.bar(x,y)
plt.show()

# The values are: (50, 52, 54)
# The pmf is: (0.5, 0.25, 0.25)
# The sum of the pmf is: 1.0.
