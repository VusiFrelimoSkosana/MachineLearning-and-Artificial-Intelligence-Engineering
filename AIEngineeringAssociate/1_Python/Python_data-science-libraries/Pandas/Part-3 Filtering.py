#we rearrange the data of x-axis not to be repetitive of the same value

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('pseudo_facebook.csv')

df

x_train=np.array(df['age'])
y_train= np.array(df['likes_received'])


#print(max(x_train))
    


x_age_train_count= np.array(df['age'].value_counts())

mean_friendships_initiated=np.zeros_like(x_age_train_count)
total_age=np.zeros_like(x_age_train_count)

j=0
age=min(x_train)

for i in range(len(x_age_train_count)):
    
    total_age[j]=age
    
    filt_age= (df['age']== age) #This is a series
    corresp_friendships_initiated= np.array(df.loc[filt_age,'friendships_initiated']) 
    #df.loc[filt,'tenure'] is a series

    #The above line of code i.e np.array ~ ~ converts series into a list/array
    #N.B np.array show shortened array while list[...] shows entire list
    
    friendships_initiated_count=0
    
    for friendships_initiated in corresp_friendships_initiated:
         friendships_initiated_count=  friendships_initiated_count + friendships_initiated
    
    mean= friendships_initiated_count/len(corresp_friendships_initiated)
    mean_friendships_initiated[j]= mean
    
    age= age+1
    j=j+1
    
    
print(total_age,len(total_age))
print(mean_friendships_initiated,len(mean_friendships_initiated))

plt.scatter(total_age, mean_friendships_initiated)
plt.xlabel("age")
plt.ylabel("friendships initiated")
plt.show()