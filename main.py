"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: machinelearningmastery.com
"""
import pandas as pd
import numpy as np

# In Program 24, we wrote a function that counted courses that students are currently taking. For this program, write a function that takes a DataFrame and returns a sorted list of the computer science courses taken. Each course should occur once in the list, no matter how often it occurs in the list of courses taken by the students

# csCourses(df): This function takes as input a data frame, df, that contains a column Current Courses. It returns a sorted list of unique strings. Each string is a computer science course (i.e. starts with csci) that occurs in some entry of df['Current Courses'].
def csCourses(df):
    results_ = df.loc[:,'Current Courses']
    csci_ = []
    for value_ in results_:
        courses_ = value_.split()
        for course_ in courses_:
            if(course_.startswith('csci')):
                csci_.append(course_)

    results_ = sorted(np.unique(csci_))
    return results_

# CS courses:
#  ['csci150', 'csci160', 'csci235', 'csci265', 'csci335', 'csci39542', 'csci49362', 'csci499']
