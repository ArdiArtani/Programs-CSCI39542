"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: geeksforgeeks.org
"""
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Write a function, compute_r_line(), that takes two iterables of numeric values representing the independent variable (xes) and the dependent variable (yes) and computes the slope and y-intercept of the linear regression line using ordinary least squares. See DS 8: Chapter 15 The pseudocode for this:
def compute_r_line(xes, yes):
    # Compute the standard deviation of the xes and yes. Call these sd_x and sd_y.
    sd_x = np.std(xes)
    sd_y = np.std(yes)

    # Compute the correlation, r, of the xes and yes.
    r, _ = pearsonr(xes,yes)

    # Compute the slope, m, as m = r*sd_y/sd_x.
    m = r * sd_y / sd_x

    # Compute the y-intercept, b, as b = yes[0] - m * xes[0]
    b = yes[0] - m * xes[0]

    # Return m and b.
    return m, b

s1 = [1,2,3,4,5,6,7,8,9,10]
s2 = [0,1,1,2,2,3,3,4,4,5,]
m, b = compute_r_line(s1,s2)
print(m,b)
# xes = np.array([0,10])
# yes = m*xes + b
# plt.scatter(s1,s2)
# plt.plot(xes,yes)
# plt.title(f'Regression line with m = {m:{4}.{2}} and y-intercept = {b:{4}.{2}}')
# plt.show()
