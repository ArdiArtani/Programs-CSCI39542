"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: stackoverflow
"""
import pandas as pd
import matplotlib.pyplot as plt


# The goal is to create a plot of NYC OpenData Motor Vehicle Collisions that follows this style. For example, here is the plot for January 2020 dataset:

# Your program should begin by asking the user for input and output files. It should be written to take any dataset from the NYC OpenData Motor Vehicle Collisions and produce an image that matches this style. The resulting image should be saved to the output file specified by the user.

# get file names:
input_file_ = input('Please enter input file name: ')
output_file_ = input('Please enter output file name: ')

# input_file_ = "Motor_Vehicle_Collisions_Mar_2020.csv"
# output_file_ = "output.csv"

# read csv files
df = pd.read_csv(input_file_)
boroDF = df.groupby(['BOROUGH','CRASH DATE']).count()['CRASH TIME'].unstack().transpose()

boroDF.plot()
plt.show()
