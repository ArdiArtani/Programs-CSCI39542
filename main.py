"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: p42 hints, numpy.org
"""
import numpy as np
import pandas as pd
from sklearn.svm import SVC

def compare_clf(xes, y, test_size = 0.20, random_state=66,max_iter=500):
    x_, x_test, y_, y_test = train_test_split(xes, y, random_state = random_state, test_size = test_size)

    # grab LogisticRegression score
    clf = LogisticRegression(max_iter = max_iter)
    clf.fit(x_,y_)
    logistic_score_ = clf.score(x_test, y_test)

    # grab SVC score
    clf_svc_ = SVC()
    clf_svc_.fit(x_,y_)
    svc_score_ = clf_svc_.score(x_test, y_test)

    return logistic_score_, svc_score_
