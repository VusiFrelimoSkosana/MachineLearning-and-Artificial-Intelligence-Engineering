import pandas as pd

df=pd.read_csv('framingham.csv')

df  #this line put the date on the table

print(df.shape) #size if the rows and columns

print(df.info())  #tells about the info of the data i.e data type of each column