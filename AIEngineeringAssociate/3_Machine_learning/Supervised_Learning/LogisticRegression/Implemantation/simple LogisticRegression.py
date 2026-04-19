# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 18:35:12 2023

@author: Professor
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5,6])
y=np.array([0,0,0,1,1,1])
weight=np.zeros(2)   #w0 and wi array
#weight=0
#Define the logistic function
def logistic(z):
    sig= 1/(1+np.exp(-z))
    return sig

#Gradient of a cost function
def cost_gradient(weight,x,y):
    m=len(x)
    sigmoid=logistic(weight[0] +  weight[1]*x)
    X=np.vstack((np.ones(len(x)),x))   #for  values
    grad=(1/m) *np.dot(X,(sigmoid-y))
    print(grad)
    return grad


alpha=0.1  #learning rate
iteration=1000 #iterations

#Gradient descent
for i in range(iteration):
    weight-= alpha*cost_gradient(weight,x,y)
    
print(weight)

x_values= np.linspace(0,7,100)
y_values =logistic(weight[0]+ weight[1]*x_values)

plt.scatter(x,y,color='green')
plt.plot(x_values,y_values,color="black")
plt.title(' y vs x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend('sigmoid')
plt.show()