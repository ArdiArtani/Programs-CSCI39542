"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: pandas.pydata.org
"""
import seaborn as sns
import pandas as pd

# tripTime(start,end): This function takes two variables of type datetime and returns the difference between them.
def tripTime(start, end):
    # convert date to datatime
    start_dt1_ = pd.to_datetime(start)
    end_dt2_ = pd.to_datetime(end)
    return (end_dt2_ - start_dt1_)

# weekdays(df,col): This function takes a DataFrame, df, containing the column name, col, and returns a DataFrame containing only times that fall on a weekday (i.e. Monday through Friday).


def weekdays(df, col):
    df_ = pd.to_datetime(df[col])
    results_ = df[df_.dt.dayofweek < 5]
    return results_


# pickup,dropoff,passengers,distance,fare,tip,tolls,total,color,payment,pickup_zone,dropoff_zone,pickup_borough,dropoff_borough

# taxi = sns.load_dataset('taxis')
# print(taxi.iloc[0:10])  # Print first 10 lines:
# taxi['tripTime'] = taxi.apply(
#     lambda x: tripTime(x['pickup'], x['dropoff']), axis=1)
# print(taxi.iloc[0:10])

#                 pickup              dropoff  ...  pickup_borough  dropoff_borough
# 0  2019-03-23 20:21:09  2019-03-23 20:27:24  ...       Manhattan        Manhattan
# 1  2019-03-04 16:11:55  2019-03-04 16:19:00  ...       Manhattan        Manhattan

#                 pickup              dropoff  ...  dropoff_borough        tripTime
# 0  2019-03-23 20:21:09  2019-03-23 20:27:24  ...        Manhattan 0 days 00:06:15
# 1  2019-03-04 16:11:55  2019-03-04 16:19:00  ...        Manhattan 0 days 00:07:05
