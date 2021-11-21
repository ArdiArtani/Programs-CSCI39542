"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import numpy as np
import pandas as pd

# captures85(arr): Takes an array arr (in decreasing order), computes the captured variance (cv = (arr**2)/sum(arr**2)) and returns the number of elements needed to capture more than 85% of the variance.
def captures85(arr):
    cv = (arr**2)/sum(arr**2)
    perc_ = 0
    count_ = 0
    for value_ in cv:
        if((perc_*100) < 85):
            perc_ += value_
            count_ += 1
    return count_

def averageEigenvalue(arr):
    cv = (arr**2)/sum(arr**2)
    count_ = 0
    avg_ = cv.mean()
    for value_ in cv:
        if (value_ > avg_):
            count_ += 1

    return count_

# a = np.array([585.57, 261.06, 166.31,  57.14,  48.16,  39.79,  31.71,  28.91, 24.23,  22.23,  20.51,  18.96,  17.01,  15.73,   7.72,   4.3 , 1.95,   0.04])
# array([0.76, 0.15, 0.06, 0.01, 0.01, 0.  , 0.  , 0.  ,   0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ])
# print(captures85(a))
# print(averageEigenvalue(a))
