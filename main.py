"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: stackoverflow
"""
import pandas as pd
import re

# Write two functions that will be used to clean the OpenData NYC dataset of Libraries in New York City (downloaded as CSV file). The first three lines of the CSV file look like:

# This function takes the values from the column the_geom and extracts the longitude and latitude from the string (they are surrounded by parenthesis and separated by a space, and returns the two as numerical values. For example, the function would return -73.95353074430393, 40.80297988196676 when applied to the first row of data.
def extractLatLon(row):
    geom_ = str(row['the_geom'])
    lat_, lon_= re.search(regex_, geom_).groups()
    return (float(lat_), float(lon_))


# extractTitle(row): This function concatenates the values from the columns NAME, CITY, and ZIP code into a single string, separated by a comma and space, and returns the string (to be used as the title for our visualizations). For example, when applying this function to the first data row, the return value would be: 115th Street, New York, 10026.
def extractTitle(row):
    return str(row['NAME']) + ', ' + str(row['CITY']) + ', ' + str(row['ZIP'])



# Load the csv of libary locations:
# lib = pd.read_csv('LIBRARY.csv')
# print(extractLatLon(lib))
