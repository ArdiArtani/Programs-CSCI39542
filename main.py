"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: stackoverflow, het.as.utexas.edu/HET/Software/Scipy/stats.html
"""
import numpy as np
import scipy.stats as stats
# import matplotlib.pyplot as plt

# computeSmoothing(xes,points): This function takes a numpy array xes and a list, points, of numeric values. For each p in points, the function should compute the normal probability distribution function (scipy.norm.pdf) centered at loc = p with standard deviation scale = 0.5 for all values in xes. The return value is a numpy array of the sum of these at each point.
def computeSmoothing(xes, points):
    values_ = list(xes)
    sum_ = 0.0
    for p_ in range(points[0]):
        # print(values_[p_])
        sum_ = stats.norm.pdf(values_, p_, 0.5)
    return sum_


# xes = np.linspace(0, 10, 1000)
# density = computeSmoothing(xes,[5])
# plt.plot(xes,density)
# plt.show()
