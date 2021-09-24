"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: stackoverflow, python
"""

# In lecture, we used the Pandas' function, rolling() to compute a 7-day average of subway ridership for the visualization of ridership in 2020. For this program, write three functions that take as input a Pandas' series (e.g. a column of a DataFrame) that highlights different patterns in the data:


# cumulativeAverage(column): Assumes the input is a Series of numerical data. Returns a Series with the cumulative (running) average of the values. For example, if the first 5 entries are 10,20,30,40,20, the Series that is returned would start out as 10,15,20,25,24 (since 10/1 = 10, (10+20)/2 = 15, (10+20+30)/3 = 20, (10+20+30+40)/4 = 25, (10+20+30+40+20)/5 = 24). Note that it is different that rolling() we used in class, since this function creates a value for all entries and averages across all values seen.
# def cumulativeAverage(column):
#
#     return column



# cyclicAverage(column): Assumes the input is a Series of numerical data. Returns a Series with the average of the current day with, if they exist, the value from 7 days previously and 14 days previously. That is, if they exist, for entry at index i, take the average of the values at indices i-offset, i-2*offset, and i-3*offset, as the computation. Since ridership is highly dependent on the day of the week, this averages the values of the same day in past weeks.
# def cyclicAverage(column):
    # return column




# exponentialSmoothing(column): Assumes the input is a Series of numerical data. Returns a Series with a weighted average of the previous values with the most recent values have higher weight and the older ones have lower weights. The value for the first entry, newCol[0] is column[0]. The value for subsequent entries is newCol[t+1] = 0.5*column[t+1] + 0.5*newCol[t]. For example, if we had the same Series starting the same as above, 10,20,30,40,20, our new column would start 10,15,22.5,31.25,25.625 (since the first entry is the same, 0.5*20+0.5*10 = 15, 0.5*30+0.5*15= 22.5, 0.5*40+0.5*22.5 = 31.25, 0.5*20 + 0.5*31.25 = 25.625).
# def exponentialSmoothing(column):
#     return column
