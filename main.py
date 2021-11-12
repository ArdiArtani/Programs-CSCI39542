"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import pandas as pd
import numpy as np

# Building on Program 24 and Program 28, write a function, byCourses(), that takes a DataFrame that contains students' names, number of credits completed, and current courses (a string with the course names separated by ' '), and returns a DataFrame that
# The column indices are the names of the computer science courses only, and
# The one column is NumEnrolled, the total number of students enrolled.
# No other rows or columns should be included in the DataFrame.
def byCourses(df):
    results_ = df.loc[:,'Current Courses']
    csci_ = []
    for value_ in results_:
        courses_ = value_.split()
        for course_ in courses_:
            if(course_.startswith('csci')):
                csci_.append(course_)
                # csci_[course_] +=1

    csci_unique_ = sorted(np.unique(csci_))

    csci_occ_ = []
    n = len(csci_unique_)
    for i in range(n):
        csci_occ_.append(csci_.count(csci_unique_[i]))

    results_ = [csci_unique_, csci_occ_]
    return results_



# classDF = pd.DataFrame({'Name': ["Ana","Bao","Cara","Dara","Ella","Fatima"],\
#                           '# Credits': [45,50,80,115,30,90],\
#                           'Current Courses': ["csci160 csci235 math160 jpn201",\
#                                               "csci160 csci235 cla101 germn241",\
#                                               "csci265 csci335 csci39542 germn241",\
#                                               "csci49362 csci499",\
#                                               "csci150 csci235 math160",\
#                                               "csci335 csci39542 cla101 dan102"]})
# # print(f'Starting df:\n {classDF}\n')
# print(f'CS courses:\n {byCourses(classDF)}')
# csci150      1
# csci160      2
# csci235      3
# csci265      1
# csci335      2
# csci39542    2
# csci49362    1
# csci499      1
