"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: p42 hints, numpy.org
"""
import numpy as np
import pandas as pd
import numpy.linalg as la


# transition_mx: an square array of values between 0 and 1. Each column sums to 1.
# starting_pop: an 1D array of positive numeric values that has the same length as transition_mx.
# num_years: a column name containing the dependent variable (what's being predicted) in the model. It has a default value is 1.
# The function returns an array of the population of each state after num_years.
def moving(transition_mx, starting_pop, num_years = 1):
    results_ = la.matrix_power(transition_mx, num_years) @ starting_pop
    return results_


# transition_mx: an square array of values between 0 and 1. Each row sums to 1.
# starting_pop: an 1D array of positive numeric values that has the same length as transition_mx.
# num_years: a column name containing the dependent variable (what's being predicted) in the model. It has a default value is 1.
# The function returns an array of the population of each state at the steady state. That is, it returns the eigenvector corresponding to the largest eigenvalue, scaled so that it's entries sum to 1, and then multiplied by the sum of the starting populations.
def steadyState(transition_mx, starting_pop):
    w,v = la.eig(transition_mx)
    total_ = v[:, 0]/sum(v[:, 0])
    return (total_ * sum(starting_pop))
