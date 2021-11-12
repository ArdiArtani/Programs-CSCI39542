"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: Lecture 19 Slides
"""
#Import datasets, classifiers and performance metrics:
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#Using the digits data set from sklearn:
from sklearn import datasets

# data: a numpy array that includes rows of equal size flattend arrays,
# target a numpy array that takes values 0 or 1 corresponding to the rows of data.
# test_size: the size of the test set created when the data is divided into test and training sets with train_test_split. The default value is 0.25.
# random_state: the random seed used when the data is divided into test and training sets with train_test_split. The default value is 21.
# The function returns the Area Under the Curve (AUC) computed by sklearn.metrics.roc_auc_score as well as the classifier built.
def binary_digit_clf(data, target, test_size = 0.25, random_state = 21):
    digits = data.load_digits()
    #flatten the images
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))
    #Make a DataFrame with just the binary digits:
    binaryDigits = [(d,t) for (d,t) in zip(data,digits.target) if t <= 1]
    bd,bt = zip(*binaryDigits)

    clf = LogisticRegression()
    x_, x_test, y_, y_test = train_test_split(bd, bt, random_state = random_state, test_size = test_size)
    clf.fit(x_,y_)
    y_predict_ = clf.predict(x_test)
    confuse_mx = metrics.confusion_matrix(y_test, y_predict_, labels=[1,0])
    return confuse_mx


# confuse_mx = binary_digit_clf(bd,bt)
# print(f'Confusion matrix:\n{confuse_mx}')
