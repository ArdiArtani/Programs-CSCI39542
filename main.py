"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: Lecture 19 Slides
"""
from sklearn import datasets
from sklearn.metrics import roc_auc_score

# data: a numpy array that includes rows of equal size flattend arrays,
# target a numpy array that takes values 0 or 1 corresponding to the rows of data.
# test_size: the size of the test set created when the data is divided into test and training sets with train_test_split. The default value is 0.25.
# random_state: the random seed used when the data is divided into test and training sets with train_test_split. The default value is 21.
# The function returns the Area Under the Curve (AUC) computed by sklearn.metrics.roc_auc_score as well as the classifier built.
def binary_digit_clf(data, target, test_size = 0.25, random_state = 21):
    digits_ = data.load_digits()
    return digits_
