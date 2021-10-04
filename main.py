"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: stackoverflow, het.as.utexas.edu/HET/Software/Scipy/stats.html
"""
import numpy as np
import scipy.stats as stats

# In Lecture #9 and Section 11.5, we used smoothing to visualize data. For this program, write a function that takes two arguments, an Numpy array of x-axis coordinates, and a list of numeric values, and returns the corresponding y-values for the sum of the gaussian probability distribution functions (pdf's) for each point in the list.

# computeSmoothing(xes,points): This function takes a numpy array xes and a list, points, of numeric values. For each p in points, the function should compute the normal probability distribution function (scipy.norm.pdf) centered at loc = p with standard deviation scale = 0.5 for all values in xes. The return value is a numpy array of the sum of these at each point.
def computeSmoothing(xes,points):
    data_ = list(xes)
    std_ = 0.5
    sum_ = 0.0
    for p_ in range(points[0]):
        sum_ += stats.norm.pdf(xes[p_], p_, std_)
    return sum_

# xes = np.linspace(0, 10, 1000)
# density = computeSmoothing(xes,[5])
# plt.plot(xes,density)
# plt.show()
