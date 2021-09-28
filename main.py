"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: stackoverflow, lecture8slides.pdf
"""
import pandas as pd
import matplotlib.pyplot as plt

# The goal is to create a plot of NYC OpenData Motor Vehicle Collisions that follows this style. For example, here is the plot for January 2020 dataset:

# Your program should begin by asking the user for input and output files. It should be written to take any dataset from the NYC OpenData Motor Vehicle Collisions and produce an image that matches this style. The resulting image should be saved to the output file specified by the user.

# get file names:
input_file_ = input('Please enter input file name: ')
output_file_ = input('Please enter output file name: ')

# input_file_ = "Motor_Vehicle_Collisions_Mar_2020.csv"
# output_file_ = "output.png"

# read csv files
df = pd.read_csv(input_file_)
boroDF = df.groupby(['BOROUGH', 'CRASH DATE']).count()[
                    'CRASH TIME'].unstack().transpose()

boroDF.plot()
ax_ = plt.gca()
# Did not find CSci 39542, Hunter College as a course name and Source: OpenData NYC in code as data source
plt.title('Collisions in New York City')
plt.suptitle('By borough and date in code')
fig = plt.figure()
fig.set_figheight(8)
fig.set_figwidth(12)
# plt.figure(figsize=(12, 8))
# plt.figtext(0.5, 0.01, "one text and next text", ha="center", fontsize=18, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
plt.text(0.25, 0.25, 'Course: CSci 39542, Hunter College',
         horizontalalignment='left', verticalalignment='bottom', transform=ax_.transAxes)
# plt.text("Course: CSci 39542, Hunter College")
# plt.text("Source: OpenData NYC")
plt.show()

plt.savefig(output_file_)
