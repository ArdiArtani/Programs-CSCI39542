"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import pandas as pd
import numpy as np
import scipy.stats as st

# alpha: the fraction of the distribution contained in the interval (as in scipy.stats.t.interval()). It has a default value of 95.
# mu: the mean of the normal distribution sampled. It has a default value of 0.
# sigma: the standard deviation of the normal distribution sampled. It has a default value of 1.
# size: the size of the samples. It has a default value of 10.
# trials: the number of samples. It has a default value of 100.

# This function returns:
# A list of intervals, stored as tuples of their lower and upper values (of length trials), and
# A list of length trials containing the percentage of successful predictions after each trial. That is, the ith entry has the percent of the first i trials for which the true mean (mu) is in the confidence interval computed for the sample.
def ciRuns(alpha = 0.95, mu = 0, sigma = 1, size = 10, trials = 100):

    interval_ = []
    successes_ = []
    counter_ = 0
    for trial in range(trials):
        sampData_ = np.random.normal(mu, sigma, size)
        interval_.append(st.t.interval(alpha,len(sampData_)-1, loc=np.mean(sampData_),scale=st.sem(sampData_)))
        if(interval_[trial][0] < mu < interval_[trial][1]):
            counter_ += 1
        successes_.append(counter_/trials)

    return interval_, successes_


# intervals, successes = ciRuns(trials = 20)
# print(f"intervals: {intervals}")
# print(f"successes: {successes}")
