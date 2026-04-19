import pandas as pd

df  = pd.read_csv('framingham.csv')

df


#Example of a dictionary below

people={'firstName':['Vusi', 'Bheki', 'Frelimo'],
        'lastName':['Skhosana','Jali','Thamana'],
        'email':['vusi@gmail.com','bheki@gmail.com','frelimo@gmail.com']}

print(people['firstName'])

#Data frames are more like dictioneries with more functionality

df2=pd.DataFrame(people)

df2  #shows the dictionary as a data frame

#Just like we did with referenicng people in a dictionary, now we do it for data frame

print(df2['email'])  #this shows as a series/list

print(df2[['email','firstName']]) #this shows as a data frame



#N.B if we require more info about data frame (i.e df2['email'] ,df.shape etc) we need to use print statement on other IDEs like Syder

print('This prints out the columns:', df2.columns)

#now we want to print out the rows

print(df2.iloc[0])  #iloc means integer location, this is series

print(df2.iloc[[0,1]])  #iloc means integer location, this is Data Frame

print(df2.iloc[[0,1],2])  #the email addresses of the first two rows

#now using loc

print(df2.loc[[0,1],'email']) #similary we can use the column name instead of a number


#Now appliying the mothod to csv file 'framingham'

print(df.shape)

print(df['male'])

print(df.iloc[[0,1]])

print(df.loc[[0],'male'])

print(df['male'].value_counts()) #this will count the similar responses

#we jump into slicing

print(df.loc[0:2,'male':'education']) #slicing

print(df2.loc[0:1,'firstName':'email']) 