"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: Section 16.1.1., stackoverflow
"""
import random
import numpy as np

# diceSim(D1,D2,trials) that takes as input the number of sides on die 1 (D1) and die2 (D2) and the number of trials. Your function should repeatedly sum pairs of random numbers between 1 and D1 and 1 and D2 and keep track of how many times each sum occurs. The function returns a numpy array with the fraction each sum of rolls occured.
def diceSim(D1,D2,trials):

    # create two arrays one for counting each sum pair
    sum_occurs_ = np.zeros((D1 + D2 + 1))

    # for loop from 1 to trails
    for i in range(trials):
        # random numbers for d1 and d2
        rand_d1_ = random.randint(1, D1)
        rand_d2_ = random.randint(1, D2)
        pair_sum_ = rand_d1_ + rand_d2_

        # add +1 for pair to results array
        sum_occurs_[pair_sum_] += 1

    results_ = np.zeros(D1 + D2 + 1)
    # calculate fraction for each sum
    for i in range(D1 + D2 + 1):
        if(sum_occurs_[i] != 0):
            results_[i] = (sum_occurs_[i] / trials)

    return list(results_)



# diceSim(6,6,10000)
