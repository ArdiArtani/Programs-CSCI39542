"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""

# numComponents: the number of componets used in the approximation. Expecting a value between 0 and 64.
# coefficients: an array of coefficients, outputted from PCA().
# mean: an array representing the mean of the dataset.
# components: an array of the components computed by PCA() analysis.
# The function returns the approximation image (flattened array) of the mean and sum of the first numComponents terms (i.e. coefficients[i] * components[i]).


def approxDigits(numComponents, coefficients, mean, components):

    sum_ = 0
    for comp_ in range(numComponents):
        sum_ += coefficients[comp_] * components[comp_]

    sum_ = sum_ + mean
    return sum_
