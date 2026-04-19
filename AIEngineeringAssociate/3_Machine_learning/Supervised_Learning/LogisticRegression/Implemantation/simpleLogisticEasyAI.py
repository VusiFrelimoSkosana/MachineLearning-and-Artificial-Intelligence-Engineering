# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:57:29 2023

@author: Professor
"""

import numpy as np
import matplotlib.pyplot as plt

from easyAI.simpleLogistic import cost_gradient
from easyAI.simpleLogistic import logistic

x=np.array([1,2,3,4,5,6])
y=np.array([0,0,0,1,1,1])
weight=np.zeros(2)   #w0 and wi array

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