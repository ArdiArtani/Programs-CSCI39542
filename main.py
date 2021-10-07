"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: n/a
"""
import pandas as pd

# The program should open the file name provided by the user. Next, the program should copy the input file and create two new columns: percent_tip, which is 100*tip_amount/fare_amount and percent_fare, which is 100*fare_amount/total_amount. Your program should write out a new CSV file (with the name provided by the user) with the original columns as well as the two newly computed ones.
input_ = input('Enter input file name:')
output_ = input('Enter output file name:')
# input_ = 'taxi_new_years_day_2020.csv'
# output_ = 'taxi_Jan2020_with_percents.csv'

# read input file
df = pd.read_csv(input_)

# calculate tip and fare
df['percent_tip'] = ((df['tip_amount'] * 100) / df['fare_amount']).round(2)
df['percent_fare'] = ((df['fare_amount'] * 100) / df['total_amount']).round(2)

df.to_csv(output_, index=False)
