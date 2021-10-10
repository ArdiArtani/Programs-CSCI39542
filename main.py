"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: Section 16.1.1.
"""
import random
import numpy as np
import matplotlib.pyplot as plt

# diceSim(D1,D2,trials) that takes as input the number of sides on die 1 (D1) and die2 (D2) and the number of trials. Your function should repeatedly sum pairs of random numbers between 1 and D1 and 1 and D2 and keep track of how many times each sum occurs. The function returns a numpy array with the fraction each sum of rolls occured.
def diceSim(D1,D2,trials):

    # create two arrays one for counting each sum pair, and store all trials
    results_ = []
    trails_ = []

    # for loop from 1 to trails
    for i in range(trials):
        # random numbers for d1 and d2
        rand_d1_ = random.randint(1, D1)
        rand_d2_ = random.randint(1, D2)
        pair_sum_ = rand_d1_ + rand_d2_
        # append sum to trails array
        trails_.append(pair_sum_)

    # add plus one since range does not include 12
    # assigned 0.0 for 0 and 1; division By Zero
    for trial_ in range(D1 + D2 + 1):
        if(trial_ == 0 or trial_ == 1):
            results_.append(0.0)
        else:
            results_.append(trial_ / trails_.count(trial_))

    return results_



print(diceSim(6,6,10000))
