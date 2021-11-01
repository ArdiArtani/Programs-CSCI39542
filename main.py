"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# In Lectures #14 and #15, we discussed the hypothesis that NYC public schools have lower attendance on Fridays. For this program, write a function that takes a DataFrame of school attendance records (following the format from NYC OpenData) and returns the correlation coefficent between the day of the week and daily attendance (computed as a percentage of students present of those enrolled at the school).

# This function takes a DataFrame df, with columns School DBN, Date, Enrolled, Absent, and Present.
# The function computes the attendance as a percentage of students present over students enrolled, and calculates the day of the week for each date. The function returns the correlation coefficient of the two.
def attendCorr(df):
    # date_ = pd.to_datetime(df['Date'])
    # date_ = date_.dt.dayofweek
    df['Date'] = pd.to_datetime(df['Date'].apply(str))
    df['Date'] = df['Date'].dt.dayofweek
    df['Attending'] = (df['Present'] / df['Enrolled']) * 100
    r_, _ = pearsonr(df['Date'], df['Attending'])
    return r_


# When read in from the CSV, the columns may be stored as a string. Cast as a datetime object (e.g. pd.to_datetime()), to use the functionality. You may need to specify the format, since the DOE stored dates as YYYYMMDD (see Panda Docs).

# For datetime objects, you can access properties such as day of the week using dt prefix, similar to .str similar to .str to use string methods and properties (e.g. dt.dayofweek). See the Python Docs: date time functionality for more details.

# In Lecture #15, we introduced several ways to add features to datasets to aid in the analysis. For this program, add a new column that indicates the days of the week: 0 for Monday, 1 for Tuesday, ... 6 for Sunday (a useful function for this is: dt.dayofweek)).

# df = pd.read_csv('dailyAttendanceManHunt2018.csv')
# print(attendCorr(df))
