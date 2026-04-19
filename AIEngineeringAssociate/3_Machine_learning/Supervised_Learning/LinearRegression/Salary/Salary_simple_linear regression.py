
import pandas as pd
import numpy as np
from sklearn import linear_model #This is the linear model


import matplotlib.pyplot as plt


df=pd.read_csv('Salary.csv')

df

x= df['YearsExperience']
y=df['Salary']


reg= linear_model.LinearRegression()

reg.fit(df[['YearsExperience']], df['Salary'])

print(df[['YearsExperience']])

k=reg.predict(df[['YearsExperience']]) #Predicted values
print('predicted values of differenct years of experience are: ', k)

a=reg.predict([[5.5]])  #it must be a two dimensional i.e [[5]] instead of just 5

print('The predicted value at 5.5 yesrs of experience by the model is: ', a)


#We want to find the equation of linear regression
m=reg.coef_ #regression coeficient

print('The gradient or the regression coeficient "m" is: ', m)

c=reg.intercept_ #point of y-intercept

print("The intercept 'c' of the fitted line is: ", c)

#So now we want to prove that the predicted value was correct

#We use the equation m*x+c

print("m*x+c is", m*(5.5)+c) #alternative method to predict income in 5.5 years

y_line=m*x+ c*np.ones_like(x) #ones_like gives off the same length as array x

r2_score= reg.score(df[['YearsExperience']],y) #it's in 2D array

#The r2 score is 0.965, which is ~ 97% of he variation

print('The r2 is', r2_score)

#computing the standard deviation

residuals=np.zeros_like(x)

for i in range(len(x)):
    residuals[i]= ((y[i] - y_line[i])**2)

sum_of_squares=0

for i in residuals:
    sum_of_squares= sum_of_squares + i
    
print('The sum of squares is: ',sum_of_squares) #This is the standard deviation

#computing variance
n=len(x)
variance=sum_of_squares/n

print('The variance is: ',variance)

#plotting
plt.scatter(x,y, label='Scatter plot')
plt.xlabel("Years of Experience")
plt.ylabel('Salary')
plt.title('Salary vs Years of Experience')
plt.plot(x,k, color='red', label='Best fit line')
plt.legend()
plt.show()

