"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: From textbook.ds100.org: 6.3 SQL Joins
"""

import pandas as pd
import pandasql as psql

# get file names:
inFile_1_ = input('Please enter first file name: ')
inFile_2_ = input('Please enter second file name: ')
prefix_ = input('Please output file prefix: ')

# inFile_1_ = "nta.csv"
# inFile_2_ = "restaurants30July.csv"
# prefix_ = "selected"

# read csv files
res_table_ = pd.read_csv(inFile_1_)
nta_table_ = pd.read_csv(inFile_2_)

# Save the NTA column from the restaurant inspection table to the output file prefix+"1.csv" where prefix holds the value specified by the user.
query = 'SELECT NTA FROM res_table_'
results_1_ = psql.sqldf(query)
results_1_.to_csv(prefix_+"1.csv", index=False)

# Save the count of unique NTAs in the restaurant health inspection table to the output file prefix+"2.csv" where prefix holds the value specified by the user. (Note this will have a single column and a single value.)
query = 'SELECT count(distinct NTA) FROM nta_table_'
results_2_ = psql.sqldf(query)
results_2_.to_csv(prefix_+"2.csv", index=False)

# Save the NTA column and the count of the distinct restaurants from the restaurant inspection table to the output file prefix+"3.csv" where prefix holds the value specified by the user. (Hint: how can you use GROUP BY to organize the output?)
query = 'SELECT NTA, count(distinct DBA) as cnt_restaurants FROM res_table_ WHERE NTA IS NOT NULL GROUP BY NTA ORDER BY DBA'
results_3_ = psql.sqldf(query)
results_3_.to_csv(prefix_+"3.csv", index=False)

# Save the number of rows in the NTA table and the number of unique NTAs in the NTA table to the output file prefix+"4.csv" where prefix holds the value specified by the user. (Note this will have a two rows and two columns.)
query = 'SELECT count(ALL) as num_rows, count(distinct n.NTA) as num_ntas FROM nta_table_ as n INNER JOIN res_table_ as r ON n.NTA = r.NTA GROUP BY n.NTA'
results_4_ = psql.sqldf(query)
results_4_.to_csv(prefix_+"4.csv", index=False)

# Save the restaurant name and its NTA which can be found via a LEFT JOIN of the restaurant inspection table and NTA table. Save the results to the output file prefix+"5.csv" where prefix holds the value specified by the user. (Hint: join on the NTA code found in both (but using slightly different names). Your output should have two columns.)
query = 'SELECT n.NTA, n.NTA_Name FROM res_table_ as r LEFT JOIN nta_table_ as n ON n.NTA = r.NTA GROUP BY n.NTA'
results_5_ = psql.sqldf(query)
results_5_.to_csv(prefix_+"5.csv", index=False)

# Building on the result from 5) above, keep the LEFT JOIN as is, do one more level of aggregation, so that the end result contains 3 columns (unique NTA code, unique NTA description, and the count distinct restaurants as grouped by the first 2 columns). Save result to the output file prefix+"6.csv" where prefix holds the value specified by the user.
query = 'SELECT distinct n.NTA AS nta_code, r."CUISINE DESCRIPTION" AS nta_description, count(distinct r.DBA) AS cnt_restaurants FROM res_table_ AS r LEFT JOIN nta_table_ AS n ON n.NTA = r.NTA GROUP BY nta_code, nta_description'
results_6_ = psql.sqldf(query)
results_6_.to_csv(prefix_+"6.csv", index=False)


# .
