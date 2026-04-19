import pandas as pd

df =pd.read_csv('framingham.csv')

df  #This show the table

print(df.shape)  #shows the number of rows and columns
print(df.info())  # shows the info of the data i.e data type