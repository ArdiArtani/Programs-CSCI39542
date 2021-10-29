"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import pandas as pd
import numpy as np

# df: a DataFrame that including the specified column.
# colName: a column name of the specified DataFrame,
# k: the size of the sample. It has a default value of 10.
# n: the number of samples. It has a default value of 1000.
# It takes the sample size k and the numbers of samples, of n, a DataFrame, df, and and generates n samples of size k, computes the sample mean of each, and returns a numpy array of those means.
def sampleMeans(df, colName, k=10, n=1000):

    results_ = []
    for i in range(n):
        results_.append(df[colName].sample(n = k).mean())

    return list(results_)

# nd = [np.random.normal() for i in range(1000)]
# ed = [np.random.exponential() for i in range(1000)]
# df = pd.DataFrame({ "nd" : nd, "ed" : ed})
# print(sampleMeans(df, 'nd', k = 5, n=5))
# print(sampleMeans(df, 'nd', k = 10, n=5))

# [ 0.18006227 -0.02046562  0.13301251  0.52114451  0.47197969]
# [ 0.06028354 -0.48566047  0.02343676 -0.28361692  0.25259547]
