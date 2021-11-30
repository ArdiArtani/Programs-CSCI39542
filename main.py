"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import pandas as pd
from sklearn.manifold import MDS
from scipy.spatial.distance import cdist

# 1.find the distance matrix w / cdist(points, points, metric)
# 2.then do the MDS thing like we did w / logisticRegression() or SVD() for other assignments
# The parameters you put in are for random_state and dissimilarity(look at the MDS documentation there are only 2 things you can put dissimilarity as)
# 3.take the distance matrix and use fit_transform on it


# This function has three inputs, fits the data, and returns the embedded coordinates:
# points: a numpy array representing the features/coordinates of the input.
# metric: the metric used to compute the distance matrix.
# The default value is 'euclidean'. Other common values are 'hamming' and 'cityblock'.
# random_state: the random seed used when instantiating the MDS analysis.
# The function first computes the distance matrix for points, using the specified distance as a parameter to scipy.spatial.distance.cdist.
# The distance matrix is used to fit the MDS model and the result of fit_transform is returned.
def makeMDS(points, metric='euclidean', random_state=25):

    # cdist_ = cdist(points, points, metric)
    return 0


# makeDisplayDF(df,md_fit,legs): This function has three inputs and returns a DataFrame:
# df: a DataFrame that includes the column member that contains the legislator ID of the member.
# md_fit: an array of fitted coordinates, in the same order as df.
# legs: a DataFrame containing information about the legislators that contains columns leg_id with the legislator's ID and party containing the legislator's party.
# The function returns a DataFrame to use for plotting with columns x (storing md_fit[:,0]), y (storing md_fit[:,1]), party (storing the party affiliation of the legislator).
def makeDisplayDF(df, md_fit, legs):

    return 0


# df = pd.read_csv('vote_pivot.csv')
# votes = df.drop('member', axis=1).to_numpy()
#
# legs = pd.read_csv('legislators.csv')[['leg_id', 'party']]
# #Fit to Euclidean distances:
# md_fit = makeMDS(votes)
# vote2d = makeDisplayDF(df, md_fit, legs)
#
# #Fit to Hamming distances:
# md_fit = makeMDS(votes, metric="hamming")
# vote2d = makeDisplayDF(df, md_fit, legs)
#
# #Fit to Manhattan distances:
# md_fit = makeMDS(votes, metric="cityblock")
# vote2d = makeDisplayDF(df, md_fit, legs)
