"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: stackoverflow
"""
import pandas as pd
import numpy as np

# dropNeg(xS,yS): This function takes two iterables, xS and yS of numeric values. If any entry is not positive in either iterable, that indexed value is dropped from both series. The results are returned as two separate iterables. To do this, first zip the series together, drop all the pairs with zero or negative values, and then unzip to return series with only positive values.
# For example, if xS contains [1,2,0,3,4] and yS contains [0,-1.5,4,3,9], then the zip(xS,yS) has entries [(1,0),(1,-1.5),(0,4),(3,3),(4,9)]. Dropping all tuples that contain non-positive values yields [(3,3),(4,9)], and the unzipped results, [3,4] and [3,9], are returned.
def dropNeg(xS, yS):
    # zipping the arrays
    zip_array_ = list(zip(xS, yS))

    pos_array_ = []
    for x, y in zip_array_:
        if (x > 0) and (y > 0):
            xy_ = [x, y]
            pos_array_.append(xy_)

    print(pos_array_)

    return pos_array_

# logScale(xS,yS): This function assumes that the inputted iterables contain numeric values, are positive and not null, and returns the np.log of each. For example, when applying this function to the inputs [3,4] and [3,9], the function returns [1.098612, 1.386294] and [1.098612,2.19722458].
def logScale(xS, yS):
    dropNeg_array_ = dropNeg(xS, yS)
    xS_ = list(np.log(dropNeg_array_[0]))
    yS_ = list(np.log(dropNeg_array_[1]))
    return (xS_, yS_)


# xS = [1,2,0,3,4]
# yS = [0,-1.5,4,3,9]
print(logScale(xS, yS))
