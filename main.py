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
    for i in arr:
        if(perc_ < 85):
            perc_ += arr[i]
            count_ += 1
    return count_


def averageEigenvalue(arr):
    cv = (arr**2)/sum(arr**2)
    count_ = 0
    avg_ = cv.mean()
    for i in arr:
        if (arr[i] > avg_):
            count_ += 1

    return count_


# a = np.array([585.57, 261.06, 166.31,  57.14,  48.16,  39.79,  31.71,  28.91,
#       24.23,  22.23,  20.51,  18.96,  17.01,  15.73,   7.72,   4.3 ,
#       1.95,   0.04])
#
# captures85(a)
# averageEigenvalue(a)
