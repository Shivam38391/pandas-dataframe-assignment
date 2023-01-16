

# you can run this script in jupyternotebook and see the resulted dataframe


import sqlalchemy
import pandas as pd
#dialect+driver://username:password@host:port/database
engine=sqlalchemy.create_engine('postgresql+psycopg2://doadmin:AVNS_AZ-3Q1oUpp9WnsReBBX@devtradingsagedb-do-user-12481132-0.b.db.ondigitalocean.com:25060/defaultdb')
date1 = "2023-01-02"
date2 = "2023-01-05"

df = pd.read_sql_table("test_assignment", engine)
df.pivot_table(index=['strike', 'instrument_type'])
x =df[df.date == date1].pivot_table(index=['strike','instrument_type'])
y = df[df.date == date2].pivot_table(index=['strike','instrument_type'])
newdf = y-x

newdf2 = newdf.reset_index()

newdf2[newdf2.strike==18000] #you can verify the results with example
newdf2 #this the resulted dataframe