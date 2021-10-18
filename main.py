"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: stackoverflow.com
"""
import pandas as pd

def computeEnrollments(df):

    # only students taking 3 or more courses
    num_courses_ = df['Current Courses'].str.split().apply(len)

    # the first that counts total number of courses the student is taking
    df['NumCourses'] = num_courses_
    results_ = df.loc[df.NumCourses >= 3]

    # the second columns has the number of computer science courses currently taking (all courses that start 'csci')
    new_csci_ = results_['Current Courses'].str.findall('csci*')
    results_['CS'] = new_csci_.str.len()

    # third column with the number of other courses the student is taking.
    results_['Other'] = (results_['NumCourses'] - results_['CS'])

    return results_


# classDF = pd.DataFrame({'Name': ["Ana", "Bao", "Cara", "Dara", "Ella", "Fatima"],
#                         '# Credits': [45, 50, 80, 115, 30, 90],
#                         'Current Courses': ["csci160 csci235 math160 jpn201",
#                                             "csci160 csci235 cla101 germn241",
#                                             "csci265 csci335 csci39542 germn241",
#                                             "csci49362 csci499",
#                                             "csci150 csci235 math160",
#                                             "csci335 csci39542 cla101 dan102"]})
# print(f'Starting df:\n {classDF}')
# print(f'Ending df:\n {computeEnrollments(classDF)}')
